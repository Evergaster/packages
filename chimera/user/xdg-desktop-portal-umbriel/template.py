pkgname = "xdg-desktop-portal-umbriel"
pkgver = "0_git20261101"
pkgrel = 0
_commit = "79f087598d596ae8a81dff1036d0ab3b5c446584"
build_style = "meson"
configure_args = ["-Dpicker=enabled"]
hostmakedepends = ["glib-devel", "meson", "pkgconf", "wayland-progs"]
makedepends = [
    "cairo-devel",
    "gtk4-devel",
    "libdrm-devel",
    "libei-devel",
    "mesa-gbm-devel",
    "nlohmann-json",
    "pipewire-devel",
    "sdbus-cpp-devel",
    "tomlplusplus-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = ["xdg-desktop-portal", "xdg-desktop-portal-gtk"]
pkgdesc = "XDG desktop portal backend for Umbriel"
license = "MIT"
url = "https://github.com/noctalia-dev/xdg-desktop-portal-umbriel"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "231286cffc2250dc02d9a56d5315999f485ae1dd153c72410be0476c0e20c161"


def post_install(self):
    self.install_license("LICENSE")
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)
