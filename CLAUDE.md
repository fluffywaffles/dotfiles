# dotfiles

personal dotfiles managed by [rcm](https://github.com/thoughtbot/rcm).

## structure

```
.
├── aliases              shell aliases
├── config/
│   ├── alacritty/       terminal emulator, bound to super+Return
│   ├── bspwm/           window manager
│   ├── conky/           system monitor
│   ├── dunst/           notification daemon
│   ├── fontconfig/      font configuration
│   ├── kitty/           terminal emulator
│   ├── picom.conf       compositor
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
└── zshrc.Darwin         macOS-specific shell config
```

## conventions

- scripts use `#!/bin/zsh` and `>&2 printf` for error messages
- `config/` maps to `~/.config/` (symlinked by rcm)
- host-specific variants are `<name>.$(uname -n)`, sourced if present
- `local/bin/` maps to `~/.local/bin/` (on PATH via zshenv)
- `rcrc` with `UNDOTTED="@ LG5k"` controls rcm symlinking

## show desktop

`local/bin/bspwm-show-desktop`, bound to super+d, shows the wallpaper with a random quote over it.

- every monitor switches to an empty desktop named `zen-<id>` after the desktop it was showing,
  created on entry and removed on dismissal, so no real desktop re-tiles and the numbered desktop
  keys cannot reach it
- the quote and citation are two `aosd_cat` processes anchored at `-p 0` with absolute coordinates:
  aosd measures against the whole X screen, so the focused monitor's origin from
  `bspc query -T -m focused` is added by hand
- the block is centred as a whole; its height comes from the wrapped line count at 1.75× the font
  size
- a backgrounded `bspc subscribe --count 1` on focus, layout and window events dismisses it, so
  super+d again, changing desktop or monitor, or a new window all end it; aosd windows are
  override-redirect and raise no events of their own
- on dismissal, windows opened on an empty desktop move to that monitor's previous desktop, and each
  monitor still on its empty desktop returns to where it was
- `~/.config/bspwm-show-desktop/placement.$(uname -n)` is sourced if present and may set the
  tunables or redefine `place_quote_block`, which owns all four coordinates
