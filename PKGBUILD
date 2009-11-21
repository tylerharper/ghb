# Contributor: Tyler Harper <tyler@cowboycoding.net>

pkgname=ghb
pkgver=20091121
pkgrel=1
pkgdesc="A github command line client"
arch=(any)
url="http://phrick.org/projects/"
license=('MIT')
depends=('python', 'python-ficcle', 'python-snooze', 'python-pystache')
makedepends=('git')
provides=('ghb-git')
source=()
md5sums=()

_gitroot="git://github.com/knobe/ghb.git"
_gitname="ghb"

build() {
    cd $startdir/src
    msg "Connecting to the $_gitname git repository..."
    git clone $_gitroot

    msg "GIT checkout done or server timeout"
    msg "Starting setup..."

    cd $_gitname
    install -D m755 ${pkgname} ${pkgdir}/usr/bin/${pkgname}

    
}

