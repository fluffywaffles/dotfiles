# tell colorizable commands to print colors during interactive sessions
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias tree='tree -C'

# add user-home-local binaries to path
export path=(${HOME}/.local/bin ${path})

# custom configuration
source ~/.zshrc.local

# platform-specific overrides (i.e. Darwin vs. Linux)
source ~/.zshrc.$(uname -s)

# hostname-specific overrides (i.e. apoplexy vs. hyperion vs. w/e)
if [[ -f ${HOME}/.zshrc.${HOST} ]]; then
  source ${HOME}/.zshrc.${HOST}
fi
