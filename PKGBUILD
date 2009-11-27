# Contributor: Tyler Harper <tyler@cowboycoding.net>

pkgname=ghb
pkgver=20091126
pkgrel=1
pkgdesc="A github command line client"
arch=(any)
url="http://phrick.org/projects/"
license=('MIT')
depends=('python' 'python-ficcle' 'python-snooze' 'python-pystache')
makedepends=('git')
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
    install -d ${pkgdir}/usr/share/${pkgname}

    cp -R templates/ ${pkgdir}/usr/share/${pkgname}/
    find ${pkgdir}/usr/share/${pkgname}/ -type d -exec chmod 755 {} \;
    find ${pkgdir}/usr/share/${pkgname}/ -type f -exec chmod 644 {} \;

    install -D -m755 ${pkgname} ${pkgdir}/usr/bin/${pkgname}
}

