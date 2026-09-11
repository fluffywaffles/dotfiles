# tell colorizable commands to print colors during interactive sessions
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias tree='tree -C'

# claude code clamps itself to 256 colors whenever ${TMUX} is set; our tmux
# advertises RGB, so take the 24-bit path instead
export CLAUDE_CODE_TMUX_TRUECOLOR=1

# Vi keybindings
bindkey -v

# Preserve keybindings even after entering and exiting vi normal mode.
bindkey '^?' backward-delete-char
bindkey '^h' backward-delete-char
bindkey '^w' backward-kill-word

# Set a keybinding that re-sources the entire zsh env.
typeset -ag _zsh_rcs=(
  ${HOME}/.zshenv
  ${HOME}/.zshrc
)
function _widget_reload-zsh-env {
  local rc
  # So long as this shell was not started with 'norcs', load rc files
  if set -o | grep '^norcs[[:space:]]\+off$' &> /dev/null; then
    for rc (${_zsh_rcs}); do source ${rc}; done
    print -f '\n» source %s' ${_zsh_rcs}
    zle accept-line
  else
    >&2 print "!! no-op: this shell was started with 'setopt norcs'"
  fi
}
zle -N reload-zsh-env _widget_reload-zsh-env
bindkey '^S' reload-zsh-env

# Aliases
source ${HOME}/.aliases

# Load FZF
[ -f ${HOME}/.fzf.zsh ] && source ${HOME}/.fzf.zsh

# Load z
source ${HOME}/.local/zsh-functions/z/z.sh

# Specifically provide ANVIL_PATH for random scripts
export ANVIL_PATH=${HOME}/.config/.foundry/bin/anvil

# Add swiftly swift versions to path
if [[ -f ${HOME}/.swiftly/env.sh ]]; then
  source ${HOME}/.swiftly/env.sh
fi

# Add google-cloud-sdk to PATH and load zsh compdefs
if [[ -f ${HOME}/Downloads/google-cloud-sdk/path.zsh.inc ]]; then
  source ${HOME}/Downloads/google-cloud-sdk/path.zsh.inc
fi
if [[ -f ${HOME}/Downloads/google-cloud-sdk/completion.zsh.inc ]]; then
  source ${HOME}/Downloads/google-cloud-sdk/completion.zsh.inc
fi

# Add Windsurf / codeium binaries to path
export path=(${HOME}/.codeium/windsurf/bin ${path})

# Add npm binaries to path
export path=(${HOME}/.npm-packages/bin ${path})

# Add cargo binaries to path (e.g. watchexec)
export path=(${HOME}/.cargo/bin ${path})

# Add foundry to path
export path=(${HOME}/.config/.foundry/bin ${path})

# Add select git-contrib binaries to path
export path=(
  /usr/share/git/diff-highlight
  ${path}
)

#
# Prompt
#

vcs_prompt_formats=(
  '%{${fg[yellow]}%}${vcs[branch]:+ ∙ }'
  '%{${fg[9]}%}'
  '${vcs[branch]}${vcs[dirty]:+*}'
  '%{${fg[11]}%}${vcs[bare]:+ !bare}'
  '%{${fg[219]}%}${vcs[worktree_root]:+ @worktree/root}'
)

# Only use unicode if we're in a decent terminal...
if [[ ${TERM} != "linux" ]]; then
  print -v PROMPT -f '%s %s%s%%{${reset_color}%%} ' \
    '%{$fg[yellow]%}▌ƒ▐'                            \
    '%{$fg[green]%}%c'                              \
    ${(j::)vcs_prompt_formats}
else
  print -v PROMPT -f '%s %s%s%%{${reset_color}%%} ' \
    '%{$fg[yellow]%}f'                              \
    '%{$fg[green]%}%c'                              \
    ${(j::)vcs_prompt_formats}
fi

#
# RPrompt (the one on the right!)
# Print battery visual indicator and vim-mode on right-hand side of prompt
#

# Load batpower (for battery strength indicators in RPROMPT)
source ${HOME}/.local/zsh-functions/batpower.zsh

# Format string for conditionally displaying version control info
vcs_rprompt_formats=(
  '${vcs[staged]:+[}'
  '%{${fg[blue]}%}${vcs[staged]:+staged}%{${reset_color}%}'
  '${vcs[staged]:+]}'
)

# Draw at start of each line print, and when keymap changes
uname=$(uname -s)
function update-rprompt {
  local match mbegin mend
  >/dev/null batpower-${uname:l}
  local normal="%{$fx[bold]$fg[blue]%}[nrm]%{$reset_color%}"
  local insert="%{$fx[bold]$fg[white]%}[ins]%{$reset_color%}"
  print -v RPROMPT -f '%s%s%s${EPS1}'                   \
    ${(j::)vcs_rprompt_formats}                         \
    ${${KEYMAP/vicmd/${normal}}/(main|viins)/${insert}} \
    "${batpower_enabled:+ }$(batpower-visual-battery)"
    # ^ wrap in quotes to preserve spaces in the output
}

# Widget functions (for when zsh redraws the prompt)
function zle-line-init zle-keymap-select {
  if [[ ${KEYMAP} == vicmd ]] || [[ ${1} == 'block' ]]; then
    print -n '\e[2 q'
  else
    print -n '\e[0 q'
  fi
  update-rprompt
  zle reset-prompt
}
function zle-line-finish {
  print -n '\e[0 q'
}

# Register the widget functions
zle -N zle-line-init
zle -N zle-keymap-select
zle -N zle-line-finish

# set up rprompt on load
update-rprompt

#
#
#### WORKTREE MAGIC
#
#


# Autoload custom git functions
autoload git-worktree-root
alias gwr='git-worktree-root --verbose'
function gwk() { cd $(gwr) }

vcs-user__precmd() {
  if [[ -n ${vcs[bare]} ]] || [[ -z ${vcs[branch]} ]]; then
    return 0
  fi
  if [[ $(git-worktree-root) = ${PWD} ]]; then
    vcs[bare]=''
    vcs[worktree_root]=true
  fi
}

function git-worktree-paths {
  typeset -A entries=($(git-worktree-entries))
  print ${(kj:\n:)entries}
}

#
# Taking advantage of the fact that there can only be one checked-out
# worktree per branch at any given time, find the worktree corresponding
# to the given branch (if any).
#
function git-worktree-create-if-not-exists {
  local match mbegin mend
  local branch=${1}
  if [[ -z ${branch} ]]; then
    print -nf '━ !! %s' 'cannot create branch with no name'
    return 1
  fi
  # get the worktree root, bail early if it does not exist
  local root=$(git-worktree-root)
  if [[ -z ${root} ]]; then
    return 1
  fi
  # find existing worktree for branch, if any
  local tree_path=$(git-worktree-find-for-branch ${branch})
  if [[ -n ${tree_path} ]]; then
    print -nf '┯ %s\n└ %s\n'                  \
      "Worktree already exists for ${branch}" \
      "Path: ./${tree_path##${root}/}"
    return 0
  fi
  # if no worktree exists, select a worktree path for it
  local target_path=${2:-$(git-worktree-default-branch-path ${branch})}
  # find an existing branch, whether local or remote
  local remotes=($(git remote))
  local extant_branches=(
    $(git-branch-list-porcelain --local)
    ${(f)"$(git for-each-ref --format='%(refname)' refs/remotes)"}
  )
  local existing=${extant_branches[(r)(refs/remotes/(${(j:|:)remotes})/|)${branch}]}
  # build the argument list for 'git-worktree add'
  local -a args
  # if the existing branch points to a remote branch, or none exists...
  if   [[ -z ${existing} ]] \
    || [[ ${existing} == refs/remotes/* ]]
  then
    # create a new branch tracking the remote branch (if any)
    args=(--track -b ${branch} ${target_path} ${existing})
  else # otherwise, the branch exists locally
    # however no worktree exists, so check it out to ${target_path}
    args=(${target_path} ${branch})
  fi
  # finally, add the new worktree
  print -nf '┯ New worktree\n├ %s\n└ %s\n' \
    "Branch: ${branch}"                    \
    "Path:   ./${target_path##$(git-worktree-root)/}"
  git worktree add ${args[@]}
}

function git-worktree-remove-for-branch {
  local flags=()
  local branch
  while true; do
    if [[ ${1} =~ ^-+.+$ ]]; then flags+=(${1}); shift;
    else break
    fi
  done
  for branch in ${@}; do
    local tree=$(git-worktree-find-for-branch ${branch})
    if [[ -z ${tree} ]]; then
      print -nf '┯ %s\n└ %s\n'                           \
        'Cannot remove worktree for branch, none exists' \
        "Branch: ${branch}"
      continue
    fi
    git worktree remove ${flags[@]} ${tree}
    rm -rf ${tree}
  done
}

function git-worktree-default-branch-path {
  local branch=${1}
  print $(git-worktree-root)/${branch}
}

function zwk {
  local root=$(git-worktree-root)
  if [[ -z ${root} ]]; then
    return 1
  fi
  local worktree_paths=($(git-worktree-paths))
  # if a worktree reference is provided, jump to the matching worktree
  if [[ -n ${1} ]]; then
    local matched_path=${worktree_paths[(r)*${1}*]}
    _z -c ${root} ${matched_path}
    return 0
  fi
  # otherwise, launch an interactive worktree selector
  local selected
  print ${(j:\n:)worktree_paths#${root}/}                               \
    | fzf                                                               \
          --reverse                                                     \
          --height 50                                                   \
          --bind 'ctrl-s:toggle-preview'                                \
          --bind 'ctrl-x:execute(print !{remove} {})+accept'            \
          --bind 'ctrl-space:execute(print !cd {})+accept'              \
          --preview 'git --git-dir={}/.git show --format=short --color' \
          --preview-window hidden,up,40                                 \
    | read selected
  if [[ ${selected} =~ '^!(.+)' ]]; then
    print -z ${selected[2,-1]}
    return 0
  elif [[ -n ${selected} && ! ${PWD##${root}/} = ${selected} ]]; then
    cd ${selected}
  fi
}

# given a branch, worktree-create-if-not-exists and then cd into it
function _zwb-default-command {
  local commands=(
    "git-worktree-create-if-not-exists ${1}"
    "cd \$(git-worktree-find-for-branch ${1})"
  )
  print ${(j: && :)commands}
}

function zwb {
  if [[ ${1} == "-" ]]; then
    cd -
    return 0
  fi
  local match mbegin mend
  # get the root of the current worktree forest, and if none, bail
  local root=$(git-worktree-root)
  if [[ -z ${root} ]]; then
    >&2 print -nf 'ERR: empty root. missing `worktree-root` link?\n'
    return 1
  fi
  # load up the list of configured remotes
  typeset -a remotes=($(git remote))
  # by default, zwb will fuzzy find on branches with worktrees
  local list=worktree-branches
  # by default, include all remotes and do not filter on name
  local named_remotes=''
  # if there is only one remote, default named_remotes to that remote
  if [[ ${#remotes} -eq 1 ]]; then
    named_remotes=${remotes[1]}
  fi
  # configure list and named_remotes with flags
  # -r -remote[s] --remote[s]   -- include remotes
  # -o -only --only {pattern}   -- only include branches matching pattern
  #                              └ separate multiple branches by pipe `|`
  while true; do
    if [[ ${1} =~ ^-*r(emotes*)*$ ]]; then shift; list=remote-branches; fi
    if [[ ${1} =~ ^-*o(nly)*$     ]]; then
      local named_remotes=${2}
      shift 2
      list+=" ${named_remotes}"
    fi
    break
  done
  # first argument after flags, if given, should be a branch name
  local branch=${1}
  # load all worktrees into an associative array of path->branch
  typeset -A worktree_entries=($(git-worktree-entries))
  # if a branch reference was provided, [create and] jump to its worktree
  if [[ -n ${branch} ]]; then
    # if a worktree does not exist for the branch, create one and cd in
    eval $(_zwb-default-command ${branch})
    return 0
  fi
  # if there is no branch given, select one interactively
  # if there are no worktree entries, automatically list remote branches
  if [[ ${#worktree_entries} -eq 0 ]]; then
    print -nf '┯ %s\n└ %s\n'                                        \
      'no local worktrees, listing branches on configured remotes.' \
      "remotes: ${named_remotes:-${remotes}}"
    list="remote-branches ${named_remotes}"
  fi
  # otherwise, launch an interactive branch selector
  local selected; _zwb-toggle-list ${=list}              \
    | fzf                                                \
          --multi                                        \
          --reverse                                      \
          --height 50                                    \
          --bind 'ctrl-s:toggle-preview'                 \
          --bind 'ctrl-t:reload(_zwb-toggle-list)'       \
          --bind 'ctrl-x:become(echo !{remove} {+})'     \
          --bind 'ctrl-space:print(!{default})+accept'   \
          --preview 'git show {} --format=short --color' \
          --preview-window hidden,50                     \
    | tr '\n' ' '                                        \
    | read selected
  # strip remote prefix from selected ref, if any, unless it names a local branch
  local remotes=($(git remote))
  if   [[ ${selected} =~ ^(${(j:|:)remotes})/(.+)$ ]] \
    && ! git show-ref --verify --quiet refs/heads/${selected}
  then branch=${match[2]} # strip the remote name, grab the branch name
  else branch=${selected} # otherwise, the whole thing is the branch name
  fi
  # prefixed with '!' means 'print the following command to the prompt'
  if [[ ${branch} =~ '^!([^ ]+) (.+)$' ]]; then
    local action=${match[1]}
    local targets=${match[2]}
    if [[ ${action} = '{default}' ]]; then
      print -z $(_zwb-default-command "'${targets}'")
    elif [[ ${action} = '{remove}' ]]; then
      print -z git-worktree-remove-for-branch ${targets}
    fi
  elif [[ -n ${branch} ]]; then
    eval $(_zwb-default-command "'${branch}'")
  fi
}

zmodload zsh/complete

compdef _gitbranches                \
  zwb                               \
  git-worktree-create-if-not-exists \
  git-worktree-find-for-branch      \
  gwa

function _gitbranches {
  branches=($(git-branch-list-porcelain))
  _describe 'branch' branches
}

compdef _worktree-paths \
  zwk

function _worktree-paths {
  worktrees=($(git-worktree-paths))
  _describe 'worktree' worktrees
}

compdef _worktree-branches \
  git-worktree-remove-for-branch

function _worktree-branches {
  branches=($(git-worktree-branches))
  _describe 'branch' branches
}

if [[ -n ${precmd_functions[(r)parse-vcs-info__precmd]} ]]; then
  precmd_functions+=(vcs-user__precmd)
fi

# platform-specific overrides (i.e. Darwin vs. Linux)
if [[ -f ${HOME}/.zshrc.$(uname -s) ]]; then
  source ${HOME}/.zshrc.$(uname -s)
fi

# hostname-specific overrides (i.e. apoplexy vs. hyperion vs. w/e)
if [[ -f ${HOME}/.zshrc.${HOST} ]]; then
  source ${HOME}/.zshrc.${HOST}
fi
