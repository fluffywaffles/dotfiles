function git-worktree-entries {
  git worktree list --porcelain \
    | grep -B2 'branch'         \
    | grep -E 'branch|worktree' \
    | sed -Ee 's\branch refs/heads/|worktree \\'
}

# all        -a -all        --all
# local      -l -local      --local
# remote[s]  -r -remote[s]  --remote[s]
function git-branch-list-porcelain {
  local filter match mbegin mend
  if   [[ ${1} =~ ^-*a(ll|)$      ]]; then         filter='(heads|remotes)'
  elif [[ ${1} =~ ^-*r(emotes*|)$ ]]; then         filter='remotes'
  elif [[ ${1} =~ ^-*l(ocal|)$ || -z ${1} ]]; then filter='heads'
  else
    >&2 print "ERROR: ${0}: unrecognized argument or flag: ${1}"
    return 1
  fi
  git show-ref                 \
    | grep -E "refs/${filter}" \
    | sed -Ee "s~[0-9a-f]+ refs/${filter}/~~"
}

function git-worktree-branches {
  typeset -A entries=($(git-worktree-entries))
  print -n ${(vj:\n:)entries}
}

typeset -Ag _zwb_lists=(
  [all-branches]='git-branch-list-porcelain --remote'
  [worktree-branches]=git-worktree-branches
)

typeset -g _zwb_current_list_file="${HOME}/.cache/zwb_current_list"
typeset -g _zwb_current_list=${${(k)_zwb_lists}[1]}
if [[ -f ${_zwb_current_list_file} ]]; then
  _zwb_current_list=$(<${_zwb_current_list_file})
fi

function _zwb-toggle-list {
  # if a valid key of _zwb_lists was passed, set _zwb_current_list to it
  if [[ -n ${1} && -n ${_zwb_lists[(i)${1}]} ]]; then
    _zwb_current_list=${1}
  fi
  # check that _zwb_current_list is a valid key of _zwb_lists
  if [[ -z ${_zwb_lists[(i)${_zwb_current_list}]} ]]; then
    print -f '┯ Invalid ${_zwb_current_list}\n└ Valid lists: (%s)\n' \
      "${(k)_zwb_lists}"
    return 1
  fi
  # invoke the list generation function defined at _zwb_current_list
  # do word-splitting so we can pass options (${=name})
  ${=_zwb_lists[${_zwb_current_list}]}
  # find the index of the current list by its key name
  typeset -i index=${${(k)_zwb_lists}[(i)${_zwb_current_list}]}
  # find the next index, remembering that zsh arrays are 1-indexed
  typeset -i next_index=$((1 + ${index} % ${#_zwb_lists}))
  # get the key in the _zwb_lists associative array at the next index
  typeset next_key=${${(Ak)_zwb_lists}[${next_index}]}
  # update _zwb_current_list to the next key
  _zwb_current_list=${next_key}
  print ${_zwb_current_list} >! ${_zwb_current_list_file}
}
