# vim: set comments=b\:##,fb\:- foldmethod=marker textwidth=100:

##
## unused configuration options and defaults.
##

## Directory to save downloads to. {{{
## If unset, a sensible OS-specific default is used.
##
## Type: Directory
## }}}
# c.downloads.location.directory = None

## Prompt the user for the download location. {{{
## If set to false, `downloads.location.directory` will be used.
##
## Type: Bool
## }}}
# c.downloads.location.prompt = True

## Remember the last used download directory. {{{
##
## Type: Bool
## }}}
# c.downloads.location.remember = True

## What to display in the download filename input. {{{
##
## Type: String
## Valid values:
##   - path: Show only the download path.
##   - filename: Show only download filename.
##   - both: Show download path and filename.
## }}}
# c.downloads.location.suggestion = 'path'

## Default program used to open downloads. {{{
## If null, the default internal handler is used. Any `{}` in the string
## will be expanded to the filename, else the filename will be appended.
##
## Type: String
## }}}
# c.downloads.open_dispatcher = None

## Where to show the downloaded files. {{{
##
## Type: VerticalPosition
## Valid values:
##   - top
##   - bottom
## }}}
# c.downloads.position = 'top'

## Automatically abort insecure (HTTP) downloads {{{
## originating from secure (HTTPS) pages. For per-domain settings, the
## relevant URL is the URL initiating the download, not the URL the
## download itself is coming from. It's not recommended to set this
## setting to false globally.
##
## Type: Bool
## }}}
# c.downloads.prevent_mixed_content = True

## Duration (in milliseconds) to wait before removing finished downloads. {{{
##
## If set to -1, downloads are never removed.
##
## Type: Int
## }}}
# c.downloads.remove_finished = -1

