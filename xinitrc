#!/bin/sh

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
setxkbmap -option ctrl:nocaps # Fuck shit up: capslock → control
${HOME}/.feh-set-background   # Set random background image
sxhkd &                       # Start simple X hotkey daemon
exec bspwm                    # Run bspwm in foreground (window manager)
