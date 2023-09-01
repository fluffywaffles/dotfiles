function git-worktree-entries {
  local prefix=${1:-'.*'}
  git worktree list --porcelain                  \
    | grep -B2 'branch'                          \
    | grep -E 'branch|worktree'                  \
    | sed -Ee 's\branch refs/heads/|worktree \\' \
    | grep -E "${prefix}"
}

# all        -a -all        --all
# local      -l -local      --local
# remote[s]  -r -remote[s]  --remote[s]
#
# {prefix}
#   a ref name prefix can be passed after the flag to filter further
#
# e.g.
#   git-branch-list-porcelain --local jordan  # matches local jordan/ branches
#   git-branch-list-porcelain --remote origin # matches remote origin/ branches
#
function git-branch-list-porcelain {
  local reftype match mbegin mend
  if   [[ ${1} =~ ^-*a(ll|)$              ]]; then shift; reftype='(heads|remotes)'
  elif [[ ${1} =~ ^-*r(emotes*|)$         ]]; then shift; reftype='remotes'
  elif [[ ${1} =~ ^-*l(ocal|)$ || -z ${1} ]]; then shift; reftype='heads'
  else
    >&2 print "ERROR: ${0}: unrecognized argument or flag: ${1}"
    return 1
  fi
  # first non-flag argument is an additional prefix after the reftype
  local prefix=${1}
  if [[ ! ${prefix} =~ ^/ ]]; then
    prefix=/${prefix} # if leading slash omitted, prepend /
  fi
  git show-ref                           \
    | grep -E "refs/${reftype}${prefix}" \
    | sed -Ee "s~[0-9a-f]+ refs/${reftype}${prefix}/~~"
}

function git-worktree-branches {
  typeset -A entries=($(git-worktree-entries ${1}))
  print -n ${(vj:\n:)entries}
}

typeset -Ag _zwb_lists=(
  [remote-branches]='git-branch-list-porcelain --remote'
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
  # if a command suffix was passed, append it to the command
  if [[ -n ${2} ]]; then
    local command_suffix=${2}
  fi
  # invoke the list generation function defined at _zwb_current_list
  # do word-splitting so we can pass options (${=name})
  ${=_zwb_lists[${_zwb_current_list}]} ${=command_suffix}
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
