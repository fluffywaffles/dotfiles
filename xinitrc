#!/usr/bin/env bash

#
# Run the random crufty xinitrc script stuff that Xorg provides
#
source ${HOME}/.xinitrc.cruft.sh

#
# Host-specific pre-window-manager configurations
#
if [[ -f ${HOME}/.xinitrc.$(uname -n) ]]; then
  source ${HOME}/.xinitrc.$(uname -n)
fi

#
# ~ Do some actually interesting configuration ~
#
# setxkbmap -option ctrl:nocaps # Fuck shit up: capslock → control
${HOME}/.feh-set-background   # Set random background image

if command -v picom; then
  picom -b &  # Start the compositor in background (if installed)
fi

if [[ -f ${HOME}/.config/sxhkd/sxhkdrc.$(uname -n) ]]; then
  sxhkd_args="${HOME}/.config/sxhkd/sxhkdrc.$(uname -n)"
fi
sxhkd ${sxhkd_args:-} &           # Start simple X hotkey daemon
exec bspwm                    # Run bspwm in foreground (window manager)
