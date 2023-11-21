# vim: set comments=b\:##,fb\:- foldmethod=marker textwidth=100:

## Automatically start playing `<video>` elements. {{{
##
## Type: Bool
## }}}
c.content.autoplay = False

## Enable the ad/host blocker. {{{
##
## Type: Bool
## }}}
c.content.blocking.enabled = True

## List of URLs to host blocklists for the host blocker. {{{
## Only used when the simple host-blocker is used (see
## `content.blocking.method`).  The file can be in one of the following
## formats:  - An `/etc/hosts`-like file - One host per line - A zip-file
## of any of the above, with either only one file, or a file   named
## `hosts` (with any extension).  It's also possible to add a local file
## or directory via a `file://` URL. In case of a directory, all files in
## the directory are read as adblock lists.  The file
## `~/.config/qutebrowser/blocked-hosts` is always read if it exists.
##
## Type: List of Url
## }}}
c.content.blocking.hosts.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']

## A list of patterns that should always be loaded, even if blocked {{{
## by the ad-/host-blocker. Local domains are always exempt from
## adblocking. Note this whitelists otherwise blocked requests, not
## first-party URLs. As an example, if `example.org` loads an ad from
## `ads.example.org`, the whitelist entry could be
## `https://ads.example.org/*`. If you want to disable the adblocker on a
## given page, use the `content.blocking.enabled` setting with a URL
## pattern instead.
##
## Type: List of UrlPattern
## }}}
c.content.blocking.whitelist = ['https://link.theatlantic.com/*']

## Which cookies to accept. {{{
## With QtWebEngine, this setting also controls other features with
## tracking capabilities similar to those of cookies; including
## IndexedDB, DOM storage, filesystem API, service workers, and AppCache.
## Note that with QtWebKit, only `all` and `never` are supported as
## per-domain values. Setting `no-3rdparty` or `no- unknown-3rdparty`
## per-domain on QtWebKit will have the same effect as `all`. If this
## setting is used with URL patterns, the pattern gets applied to the
## origin/first party URL of the page making the request, not the request
## URL. With QtWebEngine 5.15.0+, paths will be stripped from URLs, so
## URL patterns using paths will not match. With QtWebEngine 5.15.2+,
## subdomains are additionally stripped as well, so you will typically
## need to set this setting for `example.com` when the cookie is set on
## `somesubdomain.example.com` for it to work properly. To debug issues
## with this setting, start qutebrowser with `--debug --logfilter network
## --debug-flag log-cookies` which will show all cookies being set.
##
## Type: String
## Valid values:
##   - all: Accept all cookies.
##   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
##   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
##   - never: Don't accept cookies at all.
## }}}
c.content.cookies.accept = 'no-unknown-3rdparty'

## Enable JavaScript. {{{
##
## Type: Bool
## }}}
c.content.javascript.enabled = True

## Allow websites to register protocol handlers {{{
## via `navigator.registerProtocolHandler`.
##
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
## }}}
config.set('content.register_protocol_handler', True, 'https://calendar.google.com?cid=%25s')
config.set('content.register_protocol_handler', True, 'https://mail.google.com?extsrc=mailto&url=%25s')

## Allow websites to show notifications. {{{
##
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
## }}}
c.content.notifications.enabled = 'ask'
## disallow notifications
config.set('content.notifications.enabled', False, 'https://www.reddit.com')
## allow notifications
config.set('content.notifications.enabled', True, 'https://meet.google.com')
config.set('content.notifications.enabled', True, 'https://calendar.google.com')

## Allow websites to share screen content. {{{
##
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
## }}}
# c.content.desktop_capture = 'ask'

## Allow websites to record audio and video. {{{
##
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
## }}}
# c.content.media.audio_video_capture = 'ask'

## Allow websites to record audio. {{{
##
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
## }}}
# c.content.media.audio_capture = 'ask'

## Allow websites to record video. {{{
##
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
## }}}
# c.content.media.video_capture = 'ask'

##
## unused configuration options and defaults.
##

## List of URLs to ABP-style adblocking rulesets. {{{
## Only used when Brave's ABP-style adblocker is used (see
## `content.blocking.method`).  You can find an overview of available
## lists here: https://adblockplus.org/en/subscriptions - note that the
## special `subscribe.adblockplus.org` links aren't handled by
## qutebrowser, you will instead need to find the link to the raw `.txt`
## file (e.g. by extracting it from the `location` parameter of the
## subscribe URL and URL-decoding it).
##
## Type: List of Url
## }}}
# c.content.blocking.adblock.lists = ['https://easylist.to/easylist/easylist.txt', 'https://easylist.to/easylist/easyprivacy.txt']

## Block subdomains of blocked hosts. {{{
## Note: If only a single subdomain is blocked but should be allowed,
## consider using `content.blocking.whitelist` instead.
##
## Type: Bool
## }}}
# c.content.blocking.hosts.block_subdomains = True

## List of URLs to host blocklists for the host blocker. {{{
## Only used when the simple host-blocker is used (see
## `content.blocking.method`).  The file can be in one of the following
## formats:  - An `/etc/hosts`-like file - One host per line - A zip-file
## of any of the above, with either only one file, or a file   named
## `hosts` (with any extension).  It's also possible to add a local file
## or directory via a `file://` URL. In case of a directory, all files in
## the directory are read as adblock lists.  The file
## `~/.config/qutebrowser/blocked-hosts` is always read if it exists.
##
## Type: List of Url
## }}}
# c.content.blocking.hosts.lists = ['https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts']

## Which method of blocking ads should be used. {{{
## Support for Adblock Plus (ABP) syntax blocklists using Brave's Rust
## library requires the `adblock` Python package to be installed, which
## is an optional dependency of qutebrowser. It is required when either
## `adblock` or `both` are selected.
##
## Type: String
## Valid values:
##   - auto: Use Brave's ABP-style adblocker if available, host blocking otherwise
##   - adblock: Use Brave's ABP-style adblocker
##   - hosts: Use hosts blocking
##   - both: Use both hosts blocking and Brave's ABP-style adblocker
## }}}
# c.content.blocking.method = 'auto'

## Enable support for the HTML 5 web application cache feature. {{{
## An application cache acts like an HTTP cache in some sense. For
## documents that use the application cache via JavaScript, the loader
## engine will first ask the application cache for the contents, before
## hitting the network.
##
## Type: Bool
## }}}
# c.content.cache.appcache = True

## Maximum number of pages to hold in the global memory page cache. {{{
## The page cache allows for a nicer user experience when navigating
## forth or back to pages in the forward/back history, by pausing and
## resuming up to _n_ pages. For more information about the feature,
## please refer to:
## https://webkit.org/blog/427/webkit-page-cache-i-the-basics/
##
## Type: Int
## }}}
# c.content.cache.maximum_pages = 0

## Size (in bytes) of the HTTP network cache. {{{
## Null to use the default value. With QtWebEngine, the maximum supported
## value is 2147483647 (~2 GB).
##
## Type: Int
## }}}
# c.content.cache.size = None

## Allow websites to read canvas elements. {{{
## Note this is needed for some websites to work properly.
##
## Type: Bool
## }}}
# c.content.canvas_reading = True

## Store cookies. {{{
##
## Type: Bool
## }}}
# c.content.cookies.store = True

## Default encoding to use for websites. {{{
## The encoding must be a string describing an encoding such as _utf-8_,
## _iso-8859-1_, etc.
##
## Type: String
## }}}
# c.content.default_encoding = 'iso-8859-1'

## Try to pre-fetch DNS entries to speed up browsing. {{{
##
## Type: Bool
## }}}
# c.content.dns_prefetch = True

## Expand each subframe to its contents. {{{
## This will flatten all the frames to become one scrollable page.
##
## Type: Bool
## }}}
# c.content.frame_flattening = False

## Set fullscreen notification overlay timeout in milliseconds. {{{
## If set to 0, no overlay will be displayed.
##
## Type: Int
## }}}
# c.content.fullscreen.overlay_timeout = 3000

## Limit fullscreen to the browser window {{{
## (does not expand to fill the screen).
##
## Type: Bool
## }}}
# c.content.fullscreen.window = False

## Allow websites to request geolocations. {{{
##
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
## }}}
# c.content.geolocation = 'ask'

## Value to send in the `Accept-Language` header. {{{
## Note that the value read from JavaScript is always the global value.
##
## Type: String
## }}}
# c.content.headers.accept_language = 'en-US,en;q=0.9'

## Custom headers for qutebrowser HTTP requests. {{{
##
## Type: Dict
## }}}
# c.content.headers.custom = {}

## Value to send in the `DNT` header. {{{
## When this is set to true, qutebrowser asks websites to not track your
## identity. If set to null, the DNT header is not sent at all.
##
## Type: Bool
## }}}
# c.content.headers.do_not_track = True

## When to send the Referer header. {{{
## The Referer header tells websites from which website you were coming
## from when visiting them. Note that with QtWebEngine, websites can
## override this preference by setting the `Referrer-Policy:` header, so
## that any websites visited from them get the full referer. No restart
## is needed with QtWebKit.
##
## Type: String
## Valid values:
##   - always: Always send the Referer. With QtWebEngine 6.2+, this value is unavailable and will act like `same-domain`.
##   - never: Never send the Referer. This is not recommended, as some sites may break.
##   - same-domain: Only send the Referer for the same domain. This will still protect your privacy, but shouldn't break any sites. With QtWebEngine, the referer will still be sent for other domains, but with stripped path information.
## }}}
# c.content.headers.referer = 'same-domain'

## User agent to send. {{{
## The following placeholders are defined:
##   * `{os_info}`: Something like ## "X11; Linux x86_64".
##   * `{webkit_version}`: The underlying WebKit version (set to a fixed value   with QtWebEngine).
##   * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for QtWebEngine.
##   * `{qt_version}`: The underlying Qt version.
##   * `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for QtWebEngine.
##   * `{upstream_browser_version}`: The corresponding Safari/Chrome version.
##   * `{qutebrowser_version}`: The currently running qutebrowser version.
##
## The default value is equal to the unchanged user agent of QtWebKit/QtWebEngine.  Note that the
## value read from JavaScript is always the global value. With QtWebEngine between 5.12 and 5.14
## (inclusive), changing the value exposed to JavaScript requires a restart.
##
## Type: FormatString
## }}}
# c.content.headers.user_agent = 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {qt_key}/{qt_version} {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}'

## Enable hyperlink auditing (`<a ping>`). {{{
##
## Type: Bool
## }}}
# c.content.hyperlink_auditing = False

## Load images automatically in web pages. {{{
##
## Type: Bool
## }}}
# c.content.images = True

## Show javascript alerts. {{{
##
## Type: Bool
## }}}
# c.content.javascript.alert = True

## Allow JavaScript to close tabs. {{{
##
## Type: Bool
## }}}
# c.content.javascript.can_close_tabs = False

## Allow JavaScript to open new tabs without user interaction. {{{
##
## Type: Bool
## }}}
# c.content.javascript.can_open_tabs_automatically = False

## Allow JavaScript to read from or write to the clipboard. {{{
## With QtWebEngine, writing the clipboard as response to a user
## interaction is always allowed.
##
## Type: String
## Valid values:
##   - none: Disable access to clipboard.
##   - access: Allow reading from and writing to the clipboard.
##   - access-paste: Allow accessing the clipboard and pasting clipboard content.
## }}}
# c.content.javascript.clipboard = 'none'

## Log levels to use for JavaScript console logging messages. {{{
## When a JavaScript message with the level given in the dictionary key
## is logged, the corresponding dictionary value selects the qutebrowser
## logger to use. On QtWebKit, the "unknown" setting is always used. The
## following levels are valid: `none`, `debug`, `info`, `warning`,
## `error`.
##
## Type: Dict
## }}}
# c.content.javascript.log = {'unknown': 'debug', 'info': 'debug', 'warning': 'debug', 'error': 'debug'}

## Javascript messages to *not* show in the UI, {{{
## despite a corresponding `content.javascript.log_message.levels`
## setting. Both keys and values are glob patterns, with the key matching
## the location of the error, and the value matching the error message.
## By default, the https://web.dev/csp/[Content security policy]
## violations triggered by qutebrowser's stylesheet handling are
## excluded, as those errors are to be expected and can't be easily
## handled by the underlying code.
##
## Type: Dict
## }}}
# c.content.javascript.log_message.excludes = {'userscript:_qute_stylesheet': ['*Refused to apply inline style because it violates the following Content Security Policy directive: *']}

## Javascript message sources/levels to show in the qutebrowser UI. {{{
## When a JavaScript message is logged from a location matching the glob
## pattern given in the key, and is from one of the levels listed as
## value, it's surfaced as a message in the qutebrowser UI. By default,
## errors happening in qutebrowser internally are shown to the user.
##
## Type: Dict
## }}}
# c.content.javascript.log_message.levels = {'qute:*': ['error'], 'userscript:GM-*': [], 'userscript:*': ['error']}

## Use standard JavaScript modal for `alert()` and `confirm()`. {{{
##
## Type: Bool
## }}}
# c.content.javascript.modal_dialog = False

## Show javascript prompts. {{{
##
## Type: Bool
## }}}
# c.content.javascript.prompt = True

## Allow locally loaded documents to access other local URLs. {{{
##
## Type: Bool
## }}}
# c.content.local_content_can_access_file_urls = True

## Allow locally loaded documents to access remote URLs. {{{
##
## Type: Bool
## }}}
# c.content.local_content_can_access_remote_urls = False

## Enable support for HTML 5 local storage and Web SQL. {{{
##
## Type: Bool
## }}}
# c.content.local_storage = True

## Allow websites to lock your mouse pointer. {{{
##
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
## }}}
# c.content.mouse_lock = 'ask'

## Automatically mute tabs. {{{
## Note that if the `:tab-mute` command is used, the mute status for the
## affected tab is now controlled manually, and this setting doesn't have
## any effect.
##
## Type: Bool
## }}}
# c.content.mute = False

## Netrc-file for HTTP authentication. {{{
## If unset, `~/.netrc` is used.
##
## Type: File
## }}}
# c.content.netrc_file = None

## What notification presenter to use for web notifications. {{{
## Note that not all implementations support all features of
## notifications: - The `qt` and `systray` options only support showing
## one notification at the time   and ignore the `tag` option to replace
## existing notifications. - The `herbe` option only supports showing one
## notification at the time and doesn't   show icons. - The `messages`
## option doesn't show icons and doesn't support the `click` and `close`
## events.
##
## Type: String
## Valid values:
##   - auto: Tries `libnotify`, `systray` and `messages`, uses the first one available without showing error messages.
##   - qt: Use Qt's native notification presenter, based on a system tray icon. Switching from or to this value requires a restart of qutebrowser.
##   - libnotify: Shows messages via DBus in a libnotify-compatible way. If DBus isn't available, falls back to `systray` or `messages`, but shows an error message.
##   - systray: Use a notification presenter based on a systray icon. Falls back to `libnotify` or `messages` if not systray is available. This is a reimplementation of the `qt` setting value, but with the possibility to switch to it at runtime.
##   - messages: Show notifications as qutebrowser messages. Most notification features aren't available.
##   - herbe: (experimental!) Show notifications using herbe (github.com/dudik/herbe). Most notification features aren't available.
## }}}
# c.content.notifications.presenter = 'auto'

## Whether to show the origin URL for notifications. {{{
## Note that URL patterns with this setting only get matched against the
## origin part of the URL, so e.g. paths in patterns will never match.
## Note that with the `qt` presenter, origins are never shown.
##
## Type: Bool
## }}}
# c.content.notifications.show_origin = True

## Display PDF files via PDF. {{{
## js in the browser without showing a download prompt. Note that the
## files can still be downloaded by clicking the download button in the
## pdf.js viewer. With this set to `false`, the `:prompt-open-download
## --pdfjs` command (bound to `<Ctrl-p>` by default) can be used in the
## download prompt.
##
## Type: Bool
## }}}
# c.content.pdfjs = False

## Allow websites to request persistent storage quota {{{
## via `navigator.webkitPersistentStorage.requestQuota`.
##
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
## }}}
# c.content.persistent_storage = 'ask'

## Enable plugins in Web pages. {{{
##
## Type: Bool
## }}}
# c.content.plugins = False

## Request websites to minimize non-essentials animations and motion. {{{
##
## This results in the `prefers-reduced-motion` CSS media query to
## evaluate to `reduce` (rather than `no-preference`). On Windows, if
## this setting is set to False, the system-wide animation setting is
## considered.
##
## Type: Bool
## }}}
# c.content.prefers_reduced_motion = False

## Draw the background color and images also when the page is printed. {{{
##
## Type: Bool
## }}}
# c.content.print_element_backgrounds = True

## Open new windows in private browsing mode. {{{
## (which does not record visited pages.)
##
## Type: Bool
## }}}
# c.content.private_browsing = False

## Proxy to use. {{{
## In addition to the listed values, you can use a `socks://...` or
## `http://...` URL. Note that with QtWebEngine, it will take a couple of
## seconds until the change is applied, if this value is changed at
## runtime. Authentication for SOCKS proxies isn't supported due to
## Chromium limitations.
##
## Type: Proxy
## Valid values:
##   - system: Use the system wide proxy.
##   - none: Don't use any proxy
## }}}
# c.content.proxy = 'system'

## Send DNS requests over the configured proxy. {{{
##
## Type: Bool
## }}}
# c.content.proxy_dns_requests = True

## Enable quirks (such as faked user agent headers) {{{
## needed to get specific sites to work properly.
##
## Type: Bool
## }}}
# c.content.site_specific_quirks.enabled = True

## Disable a list of named quirks. {{{
##
## Type: FlagList
## Valid values:
##   - ua-whatsapp
##   - ua-google
##   - ua-slack
##   - ua-googledocs
##   - js-whatsapp-web
##   - js-discord
##   - js-string-replaceall
##   - js-array-at
##   - misc-krunker
##   - misc-mathml-darkmode
## }}}
# c.content.site_specific_quirks.skip = []

## How to proceed on TLS certificate errors. {{{
##
## Type: String
## Valid values:
##   - ask: Ask how to proceed for every certificate error (unless non-overridable due to HSTS).
##   - ask-block-thirdparty: Ask how to proceed for normal page loads, but silently block resource loads.
##   - block: Automatically block loading on certificate errors.
##   - load-insecurely: Force loading pages despite certificate errors. This is *insecure* and should be avoided. Instead of using this, consider fixing the underlying issue or importing a self-signed certificate via `certutil` (or Chromium) instead.
## }}}
# c.content.tls.certificate_errors = 'ask'

## How navigation requests to URLs with unknown schemes are handled. {{{
##
## Type: String
## Valid values:
##   - disallow: Disallows all navigation requests to URLs with unknown schemes.
##   - allow-from-user-interaction: Allows navigation requests to URLs with unknown schemes that are issued from user-interaction (like a mouse-click), whereas other navigation requests (for example from JavaScript) are suppressed.
##   - allow-all: Allows all navigation requests to URLs with unknown schemes.
## }}}
# c.content.unknown_url_scheme_policy = 'allow-from-user-interaction'

## List of user stylesheet filenames to use. {{{
##
## Type: List of File, or File
## }}}
# c.content.user_stylesheets = []

## Enable WebGL. {{{
##
## Type: Bool
## }}}
# c.content.webgl = True

## Which interfaces to expose via WebRTC. {{{
##
## Type: String
## Valid values:
##   - all-interfaces: WebRTC has the right to enumerate all interfaces and bind them to discover public interfaces.
##   - default-public-and-private-interfaces: WebRTC should only use the default route used by http. This also exposes the associated default private address. Default route is the route chosen by the OS on a multi-homed endpoint.
##   - default-public-interface-only: WebRTC should only use the default route used by http. This doesn't expose any local addresses.
##   - disable-non-proxied-udp: WebRTC should only use TCP to contact peers or servers unless the proxy server supports UDP. This doesn't expose any local addresses either.
## }}}
# c.content.webrtc_ip_handling_policy = 'all-interfaces'

## Monitor load requests for cross-site scripting attempts. {{{
## Suspicious scripts will be blocked and reported in the devtools
## JavaScript console. Note that bypasses for the XSS auditor are widely
## known and it can be abused for cross-site info leaks in some
## scenarios, see:
## https://www.chromium.org/developers/design-documents/xss-auditor
##
## Type: Bool
## }}}
# c.content.xss_auditing = False
