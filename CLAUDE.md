# dotfiles

personal dotfiles managed by [rcm](https://github.com/thoughtbot/rcm).

## structure

```
.
├── aliases              shell aliases
├── config/
│   ├── bspwm/           window manager
│   ├── conky/           system monitor
│   ├── dunst/           notification daemon
│   ├── fontconfig/      font configuration
│   ├── qutebrowser/     web browser
│   ├── sxhkd/           hotkey daemon
│   ├── systemd/user/    user systemd units
│   └── yay/             AUR helper
├── local/bin/           user scripts
├── gitconfig            git configuration
├── rcrc                 rcm configuration
├── tmux.conf            tmux configuration
├── xinitrc              X11 startup
├── zshenv               environment setup and PATH
├── zshrc                interactive shell config
├── zshrc.local          machine-local shell config
└── zshrc.Darwin         macOS-specific shell config
```

## conventions

- scripts use `#!/bin/zsh` and `>&2 printf` for error messages
- `config/` maps to `~/.config/` (symlinked by rcm)
- `local/bin/` maps to `~/.local/bin/` (on PATH via zshenv)
- `rcrc` with `UNDOTTED="@ LG5k"` controls rcm symlinking
