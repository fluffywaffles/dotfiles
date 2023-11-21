# vim: set comments=b\:##,fb\:- foldmethod=marker textwidth=100:

##
## unused configuration options and defaults.
##

## Additional arguments to pass to Qt, without leading `--`. {{{
## With QtWebEngine, some Chromium arguments (see
## https://peter.sh/experiments/chromium-command-line-switches/ for a
## list) will work.
##
## Type: List of String
## }}}
# c.qt.args = []

## Enables Web Platform features that are in development. {{{
## This passes the `--enable-experimental-web-platform-features` flag to
## Chromium. By default, this is enabled with Qt 5 to maximize
## compatibility despite an aging Chromium base.
##
## Type: String
## Valid values:
##   - always: Enable experimental web platform features.
##   - auto: Enable experimental web platform features when using Qt 5.
##   - never: Disable experimental web platform features.
## }}}
# c.qt.chromium.experimental_web_platform_features = 'auto'

## When to use Chromium's low-end device mode. {{{
## This improves the RAM usage of renderer processes, at the expense of
## performance.
##
## Type: String
## Valid values:
##   - always: Always use low-end device mode.
##   - auto: Decide automatically (uses low-end mode with < 1 GB available RAM).
##   - never: Never use low-end device mode.
## }}}
# c.qt.chromium.low_end_device_mode = 'auto'

## Which Chromium process model to use. {{{
## Alternative process models use less resources, but decrease security
## and robustness. See the following pages for more details:    -
## https://www.chromium.org/developers/design-documents/process-models -
## https://doc.qt.io/qt-6/qtwebengine-features.html#process-models
##
## Type: String
## Valid values:
##   - process-per-site-instance: Pages from separate sites are put into separate processes and separate visits to the same site are also isolated.
##   - process-per-site: Pages from separate sites are put into separate processes. Unlike Process per Site Instance, all visits to the same site will share an OS process. The benefit of this model is reduced memory consumption, because more web pages will share processes. The drawbacks include reduced security, robustness, and responsiveness.
##   - single-process: Run all tabs in a single process. This should be used for debugging purposes only, and it disables `:open --private`.
## }}}
# c.qt.chromium.process_model = 'process-per-site-instance'

## What sandboxing mechanisms in Chromium to use. {{{
## Chromium has various sandboxing layers, which should be enabled for
## normal browser usage. Mainly for testing and development, it's
## possible to disable individual sandboxing layers via this setting.
## Open `chrome://sandbox` to see the current sandbox status. Changing
## this setting is only recommended if you know what you're doing, as it
## **disables one of Chromium's security layers**. To avoid sandboxing
## being accidentally disabled persistently, this setting can only be set
## via `config.py`, not via `:set`. See the Chromium documentation for
## more details: - htt
## ps://chromium.googlesource.com/chromium/src/\+/HEAD/docs/linux/sandbox
## ing.md[Linux] - https://chromium.googlesource.com/chromium/src/\+/HEAD
## /docs/design/sandbox.md[Windows] - https://chromium.googlesource.com/c
## hromium/src/\+/HEAD/docs/design/sandbox_faq.md[FAQ (Windows-centric)]
##
## Type: String
## Valid values:
##   - enable-all: Enable all available sandboxing mechanisms.
##   - disable-seccomp-bpf: Disable the Seccomp BPF filter sandbox (Linux only).
##   - disable-all: Disable all sandboxing (**not recommended!**).
## }}}
# c.qt.chromium.sandboxing = 'enable-all'

## Additional environment variables to set. {{{
## Setting an environment variable to null/None will unset it.
##
## Type: Dict
## }}}
# c.qt.environ = {}

## Force a Qt platform to use. {{{
## This sets the `QT_QPA_PLATFORM` environment variable and is useful to
## force using the XCB plugin when running QtWebEngine on Wayland.
##
## Type: String
## }}}
# c.qt.force_platform = None

## Force a Qt platformtheme to use. {{{
## This sets the `QT_QPA_PLATFORMTHEME` environment variable which
## controls dialogs like the filepicker. By default, Qt determines the
## platform theme based on the desktop environment.
##
## Type: String
## }}}
# c.qt.force_platformtheme = None

## Force software rendering for QtWebEngine. {{{
## This is needed for QtWebEngine to work with Nouveau drivers and can be
## useful in other scenarios related to graphic issues.
##
## Type: String
## Valid values:
##   - software-opengl: Tell LibGL to use a software implementation of GL (`LIBGL_ALWAYS_SOFTWARE` / `QT_XCB_FORCE_SOFTWARE_OPENGL`)
##   - qt-quick: Tell Qt Quick to use a software renderer instead of OpenGL. (`QT_QUICK_BACKEND=software`)
##   - chromium: Tell Chromium to disable GPU support and use Skia software rendering instead. (`--disable-gpu`)
##   - none: Don't force software rendering.
## }}}
# c.qt.force_software_rendering = 'none'

## Turn on Qt HighDPI scaling. {{{
## This is equivalent to setting QT_ENABLE_HIGHDPI_SCALING=1 (Qt >= 5.14)
## in the environment. It's off by default as it can cause issues with
## some bitmap fonts. As an alternative to this, it's possible to set
## font sizes and the `zoom.default` setting.
##
## Type: Bool
## }}}
# c.qt.highdpi = False

## Disable accelerated 2d canvas to avoid graphical glitches. {{{
## On some setups graphical issues can occur on sites like Google sheets
## and PDF.js. These don't occur when accelerated 2d canvas is turned
## off, so we do that by default. So far these glitches only occur on
## some Intel graphics devices.
##
## Type: String
## Valid values:
##   - always: Disable accelerated 2d canvas
##   - auto: Disable on Qt6 < 6.6.0, enable otherwise
##   - never: Enable accelerated 2d canvas
## }}}
# c.qt.workarounds.disable_accelerated_2d_canvas = 'auto'

## Work around locale parsing issues in QtWebEngine 5. {{{
## 15.3. With some locales, QtWebEngine 5.15.3 is unusable without this
## workaround. In affected scenarios, QtWebEngine will log "Network
## service crashed, restarting service." and only display a blank page.
## However, It is expected that distributions shipping QtWebEngine 5.15.3
## follow up with a proper fix soon, so it is disabled by default.
##
## Type: Bool
## }}}
# c.qt.workarounds.locale = False

## Delete the QtWebEngine Service Worker directory on every start. {{{
## This workaround can help with certain crashes caused by an unknown
## QtWebEngine bug related to Service Workers. Those crashes happen
## seemingly immediately on Windows; after one hour of operation on other
## systems. Note however that enabling this option *can lead to data
## loss* on some pages (as Service Worker data isn't persisted) and will
## negatively impact start-up time.
##
## Type: Bool
## }}}
# c.qt.workarounds.remove_service_workers = False

