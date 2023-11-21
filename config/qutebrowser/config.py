# vim: set comments=b\:##,fb\:- foldmethod=marker textwidth=100:

## Autogenerated config.py {{{
##
## NOTE: config.py is intended for advanced users who are comfortable
## with manually migrating the config file on qutebrowser upgrades. If
## you prefer, you can also configure qutebrowser using the
## :set/:bind/:config-* commands without having to write a config.py
## file.
##
## Documentation:
##   qute://help/configuring.html
##   qute://help/settings.html
## }}}

## This is here so configs done via the GUI are still loaded. {{{
## Remove it to not load settings done via the GUI.
# }}}
config.load_autoconfig(False)

##
## source configurations from organized sub-files
##

# keybindings configuration.
config.source('config/bindings.py')
# colors configuration.
config.source('config/colors.py')
# completion configuration.
config.source('config/completion.py')
# content configuration.
config.source('config/content.py')
# downloads configuration.
config.source('config/downloads.py')
# fileselect configuration.
config.source('config/fileselect.py')
# fonts configuration.
config.source('config/fonts.py')
# hints configuration.
config.source('config/hints.py')
# input configuration.
config.source('config/input.py')
# qt configuration.
config.source('config/qt.py')
# tabs configuration.
config.source('config/tabs.py')
# url configuration.
config.source('config/url.py')

##
## general / miscellaneous configuration.
##

## Aliases for commands. {{{
## The keys of the given dictionary are the aliases, while the values are
## the commands they map to.
##
## Type: Dict
## }}}
c.aliases = {
    'w': 'session-save',
    'q': 'close',
    'qa': 'quit',
    'wq': 'quit --save',
    'wqa': 'quit --save'
}

## Time interval (in milliseconds) between auto-saves {{{
## of config/cookies/etc.
##
## Type: Int
## }}}
c.auto_save.interval = 15000

## Always restore open sites when qutebrowser is reopened. {{{
## Without this option set, `:wq` (`:quit --save`) needs to be used to
## save open tabs (and restore them), while quitting qutebrowser in any
## other way will not save/restore the session. By default, this will
## save to the session which was last loaded. This behavior can be
## customized via the `session.default_name` setting.
##
## Type: Bool
## }}}
c.auto_save.session = True

## Name of the session to save by default. {{{
## If this is set to null, the session which was last loaded is saved.
##
## Type: SessionName
## }}}
c.session.default_name = 'ephemeral'

## Backend to use to display websites. {{{
## qutebrowser supports two different web rendering engines / backends,
## QtWebEngine and QtWebKit (not recommended). QtWebEngine is Qt's
## official successor to QtWebKit, and both the default/recommended
## backend. It's based on a stripped-down Chromium and regularly updated
## with security fixes and new features by the Qt project:
## https://wiki.qt.io/QtWebEngine QtWebKit was qutebrowser's original
## backend when the project was started. However, support for QtWebKit
## was discontinued by the Qt project with Qt 5.6 in 2016. The
## development of QtWebKit was picked up in an official fork:
## https://github.com/qtwebkit/qtwebkit - however, the project seems to
## have stalled again. The latest release (5.212.0 Alpha 4) from March
## 2020 is based on a WebKit version from 2016, with many known security
## vulnerabilities. Additionally, there is no process isolation and
## sandboxing. Due to all those issues, while support for QtWebKit is
## still available in qutebrowser for now, using it is strongly
## discouraged.
##
## Type: String
## Valid values:
##   - webengine: Use QtWebEngine (based on Chromium - recommended).
##   - webkit: Use QtWebKit (based on WebKit, similar to Safari - many known security issues!).
## }}}
c.backend = 'webengine'

## When to show a changelog after qutebrowser was upgraded. {{{
##
## Type: String
## Valid values:
##   - major: Show changelog for major upgrades (e.g. v2.0.0 -> v3.0.0).
##   - minor: Show changelog for major and minor upgrades (e.g. v2.0.0 -> v2.1.0).
##   - patch: Show changelog for major, minor and patch upgrades (e.g. v2.0.0 -> v2.0.1).
##   - never: Never show changelog after upgrades.
## }}}
c.changelog_after_upgrade = 'minor'

## Load a restored tab as soon as it takes focus. {{{
##
## Type: Bool
## }}}
c.session.lazy_restore = False

##
## editor configuration for e.g. edit-url
##

## Editor (and arguments) to use for the `edit-*` commands. {{{
## The following placeholders are defined:  * `{file}`: Filename of the
## file to be edited. * `{line}`: Line in which the caret is found in the
## text. * `{column}`: Column in which the caret is found in the text. *
## `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
## Same as `{column}`, but starting from index 0.
##
## Type: ShellCommand
## }}}
c.editor.command = ['st', '-e', 'nvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']

## Encoding to use for the editor. {{{
##
## Type: Encoding
## }}}
c.editor.encoding = 'utf-8'

##
## unused configuration options and defaults.
##

## Require a confirmation before quitting the application. {{{
##
## Type: ConfirmQuit
## Valid values:
##   - always: Always show a confirmation.
##   - multiple-tabs: Show a confirmation if multiple tabs are opened.
##   - downloads: Show a confirmation if downloads are running
##   - never: Never show a confirmation.
## }}}
# c.confirm_quit = ['never']

## Delete the temporary file upon closing the editor. {{{
##
## Type: Bool
## }}}
# c.editor.remove_file = True

## Maximum time (in minutes) between two history items [...] {{{
## for them to be considered being from the same browsing session. Items
## with less time between them are grouped when being displayed in
## `:history`. Use -1 to disable separation.
##
## Type: Int
## }}}
# c.history_gap_interval = 30

## Keychains that shouldn't be shown in the keyhint dialog. {{{
## Globs are supported, so `;*` will blacklist all keychains starting
## with `;`. Use `*` to disable keyhints.
##
## Type: List of String
## }}}
# c.keyhint.blacklist = []

## Time (in milliseconds) from pressing a key to seeing the keyhint {{{
## dialog.
##
## Type: Int
## }}}
# c.keyhint.delay = 500

## Rounding radius (in pixels) for the edges of the keyhint dialog. {{{
##
## Type: Int
## }}}
# c.keyhint.radius = 6

## Level for console (stdout/stderr) logs. {{{
## Ignored if the `--loglevel` or `--debug` CLI flags are used.
##
## Type: LogLevel
## Valid values:
##   - vdebug
##   - debug
##   - info
##   - warning
##   - error
##   - critical
## }}}
# c.logging.level.console = 'info'

## Level for in-memory logs. {{{
##
## Type: LogLevel
## Valid values:
##   - vdebug
##   - debug
##   - info
##   - warning
##   - error
##   - critical
## }}}
# c.logging.level.ram = 'debug'

## Duration (in milliseconds) to show messages in the statusbar for. {{{
## Set to 0 to never clear messages.
##
## Type: Int
## }}}
# c.messages.timeout = 3000

## How to open links in an existing instance if a new one is launched. {{{
##
## This happens when e.g. opening a link from a terminal. See
## `new_instance_open_target_window` to customize in which window the
## link is opened in.
##
## Type: String
## Valid values:
##   - tab: Open a new tab in the existing window and activate the window.
##   - tab-bg: Open a new background tab in the existing window and activate the window.
##   - tab-silent: Open a new tab in the existing window without activating the window.
##   - tab-bg-silent: Open a new background tab in the existing window without activating the window.
##   - window: Open in a new window.
##   - private-window: Open in a new private window.
## }}}
# c.new_instance_open_target = 'tab'

## Which window to choose when opening links as new tabs. {{{
## When `new_instance_open_target` is set to `window`, this is ignored.
##
## Type: String
## Valid values:
##   - first-opened: Open new tabs in the first (oldest) opened window.
##   - last-opened: Open new tabs in the last (newest) opened window.
##   - last-focused: Open new tabs in the most recently focused window.
##   - last-visible: Open new tabs in the most recently visible window.
## }}}
# c.new_instance_open_target_window = 'last-focused'

## Show a filebrowser in download prompts. {{{
##
## Type: Bool
## }}}
# c.prompt.filebrowser = True

## Rounding radius (in pixels) for the edges of prompts. {{{
##
## Type: Int
## }}}
# c.prompt.radius = 8

## When/how to show the scrollbar. {{{
##
## Type: String
## Valid values:
##   - always: Always show the scrollbar.
##   - never: Never show the scrollbar.
##   - when-searching: Show the scrollbar when searching for text in the webpage. With the QtWebKit backend, this is equal to `never`.
##   - overlay: Show an overlay scrollbar. On macOS, this is unavailable and equal to `when-searching`; with the QtWebKit backend, this is equal to `never`. Enabling/disabling overlay scrollbars requires a restart.
## }}}
# c.scrolling.bar = 'overlay'

## Enable smooth scrolling for web pages. {{{
## Note smooth scrolling does not work with the `:scroll-px` command.
##
## Type: Bool
## }}}
# c.scrolling.smooth = False

## When to find text on a page case-insensitively. {{{
##
## Type: IgnoreCase
## Valid values:
##   - always: Search case-insensitively.
##   - never: Search case-sensitively.
##   - smart: Search case-sensitively if there are capital characters.
## }}}
# c.search.ignore_case = 'smart'

## Find text on a page incrementally, {{{
## renewing the search for each typed character.
##
## Type: Bool
## }}}
# c.search.incremental = True

## Wrap around at the top and bottom of the page [...] {{{
## when advancing through text matches using `:search-next` and
## `:search-prev`.
##
## Type: Bool
## }}}
# c.search.wrap = True

## Display messages when advancing through text matches [...] {{{
## at the top and bottom of the page, e.g. `Search hit TOP`.
##
## Type: Bool
## }}}
# c.search.wrap_messages = True

## Languages to use for spell checking. {{{
## You can check for available languages and install dictionaries using
## scripts/dictcli.py. Run the script with -h/--help for instructions.
##
## Type: List of String
## Valid values:
##   - af-ZA: Afrikaans (South Africa)
##   - bg-BG: Bulgarian (Bulgaria)
##   - ca-ES: Catalan (Spain)
##   - cs-CZ: Czech (Czech Republic)
##   - da-DK: Danish (Denmark)
##   - de-DE: German (Germany)
##   - el-GR: Greek (Greece)
##   - en-AU: English (Australia)
##   - en-CA: English (Canada)
##   - en-GB: English (United Kingdom)
##   - en-US: English (United States)
##   - es-ES: Spanish (Spain)
##   - et-EE: Estonian (Estonia)
##   - fa-IR: Farsi (Iran)
##   - fo-FO: Faroese (Faroe Islands)
##   - fr-FR: French (France)
##   - he-IL: Hebrew (Israel)
##   - hi-IN: Hindi (India)
##   - hr-HR: Croatian (Croatia)
##   - hu-HU: Hungarian (Hungary)
##   - id-ID: Indonesian (Indonesia)
##   - it-IT: Italian (Italy)
##   - ko: Korean
##   - lt-LT: Lithuanian (Lithuania)
##   - lv-LV: Latvian (Latvia)
##   - nb-NO: Norwegian (Norway)
##   - nl-NL: Dutch (Netherlands)
##   - pl-PL: Polish (Poland)
##   - pt-BR: Portuguese (Brazil)
##   - pt-PT: Portuguese (Portugal)
##   - ro-RO: Romanian (Romania)
##   - ru-RU: Russian (Russia)
##   - sh: Serbo-Croatian
##   - sk-SK: Slovak (Slovakia)
##   - sl-SI: Slovenian (Slovenia)
##   - sq: Albanian
##   - sr: Serbian
##   - sv-SE: Swedish (Sweden)
##   - ta-IN: Tamil (India)
##   - tg-TG: Tajik (Tajikistan)
##   - tr-TR: Turkish (Turkey)
##   - uk-UA: Ukrainian (Ukraine)
##   - vi-VN: Vietnamese (Viet Nam)
## }}}
# c.spellcheck.languages = []

## Padding (in pixels) for the statusbar. {{{
##
## Type: Padding
## }}}
# c.statusbar.padding = {'top': 1, 'bottom': 1, 'left': 0, 'right': 0}

## Position of the status bar. {{{
##
## Type: VerticalPosition
## Valid values:
##   - top
##   - bottom
## }}}
# c.statusbar.position = 'bottom'

## When to show the statusbar. {{{
##
## Type: String
## Valid values:
##   - always: Always show the statusbar.
##   - never: Always hide the statusbar.
##   - in-mode: Show the statusbar when in modes other than normal mode.
## }}}
# c.statusbar.show = 'always'

## List of widgets displayed in the statusbar. {{{
##
## Type: List of StatusbarWidget
## Valid values:
##   - url: Current page URL.
##   - scroll: Percentage of the current page position like `10%`.
##   - scroll_raw: Raw percentage of the current page position like `10`.
##   - history: Display an arrow when possible to go back/forward in history.
##   - search_match: A match count when searching, e.g. `Match [2/10]`.
##   - tabs: Current active tab, e.g. `2`.
##   - keypress: Display pressed keys when composing a vi command.
##   - progress: Progress bar for the current page loading.
##   - text:foo: Display the static text after the colon, `foo` in the example.
##   - clock: Display current time. The format can be changed by adding a format string via `clock:...`. For supported format strings, see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes[the Python datetime documentation].
## }}}
# c.statusbar.widgets = ['keypress', 'search_match', 'url', 'scroll', 'history', 'tabs', 'progress']

## Open new tabs (middleclick/ctrl+click) in the background. {{{
##
## Type: Bool
## }}}
# c.tabs.background = True

## Hide the window decoration. {{{
## This setting requires a restart on Wayland.
##
## Type: Bool
## }}}
# c.window.hide_decoration = False

## Format to use for the window title. {{{
## The same placeholders like for `tabs.title.format` are defined.
##
## Type: FormatString
## }}}
# c.window.title_format = '{perc}{current_title}{title_sep}qutebrowser'

## Set the main window background to transparent. {{{
## This allows having a transparent tab- or statusbar (might require a
## compositor such as picom). However, it breaks some functionality such
## as dmenu embedding via its `-w` option. On some systems, it was
## additionally reported that main window transparency negatively affects
## performance.  Note this setting only affects windows opened after
## setting it.
##
## Type: Bool
## }}}
# c.window.transparent = False

## Default zoom level. {{{
##
## Type: Perc
## }}}
# c.zoom.default = '100%'

## Available zoom levels. {{{
##
## Type: List of Perc
## }}}
# c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%', '110%', '125%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']

## Number of zoom increments to divide the mouse wheel movements to. {{{
##
## Type: Int
## }}}
# c.zoom.mouse_divider = 512

## Apply the zoom factor on a frame only to the text or to all content. {{{
##
## Type: Bool
## }}}
# c.zoom.text_only = False
