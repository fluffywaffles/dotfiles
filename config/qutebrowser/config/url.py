# vim: set comments=b\:##,fb\:- foldmethod=marker textwidth=100:

##
## unused configuration options and defaults.
##

## What search to start when something else than a URL is entered. {{{
##
## Type: String
## Valid values:
##   - naive: Use simple/naive check.
##   - dns: Use DNS requests (might be slow!).
##   - never: Never search automatically.
##   - schemeless: Always search automatically unless URL explicitly contains a scheme.
## }}}
# c.url.auto_search = 'naive'

## Page to open if :open -t/-b/-w is used without URL. {{{
## Use `about:blank` for a blank page.
##
## Type: FuzzyUrl
## }}}
# c.url.default_page = 'https://start.duckduckgo.com/'

## URL segments where `:navigate increment/decrement` [...] {{{
## will search for a number.
##
## Type: FlagList
## Valid values:
##   - host
##   - port
##   - path
##   - query
##   - anchor
## }}}
# c.url.incdec_segments = ['path', 'query']

## Open base URL of the searchengine [...] {{{
## if a searchengine shortcut is invoked without parameters.
##
## Type: Bool
## }}}
# c.url.open_base_url = False

## Search engines which can be used via the address bar. {{{
## Maps a search engine name (such as `DEFAULT`, or `ddg`) to a URL with
## a `{}` placeholder. The placeholder will be replaced by the search
## term, use `{{` and `}}` for literal `{`/`}` braces.  The following
## further placeholds are defined to configure how special characters in
## the search terms are replaced by safe characters (called 'quoting'):
## * `{}` and `{semiquoted}` quote everything except slashes; this is the
## most   sensible choice for almost all search engines (for the search
## term   `slash/and&amp` this placeholder expands to `slash/and%26amp`).
## * `{quoted}` quotes all characters (for `slash/and&amp` this
## placeholder   expands to `slash%2Fand%26amp`). * `{unquoted}` quotes
## nothing (for `slash/and&amp` this placeholder   expands to
## `slash/and&amp`). * `{0}` means the same as `{}`, but can be used
## multiple times.  The search engine named `DEFAULT` is used when
## `url.auto_search` is turned on and something else than a URL was
## entered to be opened. Other search engines can be used by prepending
## the search engine name to the search term, e.g. `:open google
## qutebrowser`.
##
## Type: Dict
## }}}
# c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}'}

## Page(s) to open at the start. {{{
##
## Type: List of FuzzyUrl, or FuzzyUrl
## }}}
# c.url.start_pages = ['https://start.duckduckgo.com']

## URL parameters to strip with `:yank url`. {{{
##
## Type: List of String
## }}}
# c.url.yank_ignored_parameters = ['ref', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'utm_name']

