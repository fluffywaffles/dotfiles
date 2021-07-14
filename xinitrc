#!/bin/sh

#
# Run the random crufty xinitrc script stuff that Xorg provides
#
source ${HOME}/.xinitrc.cruft.sh

#
# ~ Do some actually interesting configuration ~
#

# Rotate connected output(s) NOTE: this should be hostname-specific.
# xrandr -q                                           \
#   | grep "\bconnected\b"                            \
#   | while read -r monitor
#   do echo $monitor                                  \
#     | cut -d' ' -f1                                 \
#     | xargs -I {} xrandr --output {} --rotate left
#   done

setxkbmap -option ctrl:nocaps # Fuck shit up: capslock → control
${HOME}/.feh-set-background   # Set random background image
sxhkd &                       # Start simple X hotkey daemon
exec bspwm                    # Run bspwm in foreground (window manager)
