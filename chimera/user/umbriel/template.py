pkgname = "umbriel"
pkgver = "0_git20261104"
pkgrel = 0
_commit = "b6c4b7ddfb03e6bacf4fd0c76a13dca3a29f172f"
build_style = "meson"
configure_args = [
    "-Djemalloc=disabled",
    "-Dharness=disabled",
    "-Dtracy=disabled",
]
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "cairo-devel",
    "lcms2-devel",
    "libdisplay-info-devel",
    "libdrm-devel",
    "libei-devel",
    "libinput-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "mesa-devel",
    "mesa-gbm-devel",
    "nlohmann-json",
    "pango-devel",
    "pixman-devel",
    "tomlplusplus-devel",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.20-devel",
    "xcb-util-wm-devel",
]
depends = ["dbus", "xwayland-satellite"]
pkgdesc = "Wayland compositor with a custom effects renderer"
license = "MIT"
url = "https://github.com/noctalia-dev/umbriel"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "1cfbf9388ff0837107316cbbeb6ec8c75fd2ca9ed94026c167d85cf2007758fd"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("umbrielfx/LICENSE", name="LICENSE.umbrielfx")
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)
