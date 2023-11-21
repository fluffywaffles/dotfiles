# vim: set comments=b\:##,fb\:- foldmethod=marker textwidth=100:

##
## fileselect configuration (unused).
##

## Command (and arguments) to use for selecting a single folder in forms. {{{
##
## The command should write the selected folder path to the specified
## file or stdout. The following placeholders are defined: * `{}`:
## Filename of the file to be written to. If not contained in any
## argument, the   standard output of the command is read instead.
##
## Type: ShellCommand
## }}}
# c.fileselect.folder.command = ['xterm', '-e', 'ranger', '--choosedir={}']

## Handler for selecting file(s) in forms. {{{
## If `external`, then the commands specified by
## `fileselect.single_file.command`, `fileselect.multiple_files.command`
## and `fileselect.folder.command` are used to select one file, multiple
## files, and folders, respectively.
##
## Type: String
## Valid values:
##   - default: Use the default file selector.
##   - external: Use an external command.
## }}}
# c.fileselect.handler = 'default'

## Command (and arguments) to use for selecting multiple files in forms. {{{
##
## The command should write the selected file paths to the specified file
## or to stdout, separated by newlines. The following placeholders are
## defined: * `{}`: Filename of the file to be written to. If not
## contained in any argument, the   standard output of the command is
## read instead.
##
## Type: ShellCommand
## }}}
# c.fileselect.multiple_files.command = ['xterm', '-e', 'ranger', '--choosefiles={}']

## Command (and arguments) to use for selecting a single file in forms. {{{
##
## The command should write the selected file path to the specified file
## or stdout. The following placeholders are defined: * `{}`: Filename of
## the file to be written to. If not contained in any argument, the
## standard output of the command is read instead.
##
## Type: ShellCommand
## }}}
# c.fileselect.single_file.command = ['xterm', '-e', 'ranger', '--choosefile={}']

