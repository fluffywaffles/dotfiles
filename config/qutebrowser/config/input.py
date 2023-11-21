# vim: set comments=b\:##,fb\:- foldmethod=marker textwidth=100:

##
## unused configuration options and defaults.
##

## Allow Escape to quit the crash reporter. {{{
##
## Type: Bool
## }}}
# c.input.escape_quits_reporter = True

## Which unbound keys to forward to the webview in normal mode. {{{
##
## Type: String
## Valid values:
##   - all: Forward all unbound keys.
##   - auto: Forward unbound non-alphanumeric keys.
##   - none: Don't forward any keys.
## }}}
# c.input.forward_unbound_keys = 'auto'

## Enter insert mode if an editable element is clicked. {{{
##
## Type: Bool
## }}}
# c.input.insert_mode.auto_enter = True

## Leave insert mode if a non-editable element is clicked. {{{
##
## Type: Bool
## }}}
# c.input.insert_mode.auto_leave = True

## Automatically enter insert mode if an editable element is focused {{{
## after loading the page.
##
## Type: Bool
## }}}
# c.input.insert_mode.auto_load = False

## Leave insert mode when starting a new page load. {{{
## Patterns may be unreliable on this setting, and they may match the url
## you are navigating to, or the URL you are navigating from.
##
## Type: Bool
## }}}
# c.input.insert_mode.leave_on_load = True

## Switch to insert mode when clicking flash and other plugins. {{{
##
## Type: Bool
## }}}
# c.input.insert_mode.plugins = False

## Include hyperlinks in the keyboard focus chain when tabbing. {{{
##
## Type: Bool
## }}}
# c.input.links_included_in_focus_chain = True

## Interpret number prefixes as counts for bindings. {{{
## This enables for vi- like bindings that can be prefixed with a number
## to indicate a count. Disabling it allows for emacs-like bindings where
## number keys are passed through (according to
## `input.forward_unbound_keys`) instead.
##
## Type: Bool
## }}}
# c.input.match_counts = True

## Whether the underlying Chromium should handle media keys. {{{
## On Linux, disabling this also disables Chromium's MPRIS integration.
##
## Type: Bool
## }}}
# c.input.media_keys = True

## Mode to change to when focusing on a tab/URL changes. {{{
##
## Type: String
## Valid values:
##   - normal
##   - insert
##   - passthrough
## }}}
# c.input.mode_override = None

## Enable back and forward buttons on the mouse. {{{
##
## Type: Bool
## }}}
# c.input.mouse.back_forward_buttons = True

## Enable Opera-like mouse rocker gestures. {{{
## This disables the context menu.
##
## Type: Bool
## }}}
# c.input.mouse.rocker_gestures = False

## Timeout (in milliseconds) for partially typed key bindings. {{{
## If the current input forms only partial matches, the keystring will be
## cleared after this time. If set to 0, partially typed bindings are
## never cleared.
##
## Type: Int
## }}}
# c.input.partial_timeout = 0

## Enable spatial navigation. {{{
## Spatial navigation consists in the ability to navigate between
## focusable elements, such as hyperlinks and form controls, on a web
## page by using the Left, Right, Up and Down arrow keys. For example, if
## a user presses the Right key, heuristics determine whether there is an
## element they might be trying to reach towards the right and which
## element they probably want.
##
## Type: Bool
## }}}
# c.input.spatial_navigation = False

