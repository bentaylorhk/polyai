pkgname=polyai
pkgver=0.1.0
pkgrel=1
pkgdesc="Script which produces a bash command described by a given prompt using OpenAI API."
arch=('any')
url="https://github.com/bentaylorhk/polyai"
license=('MIT')
depends=('python' 'python-openai' 'python-pydantic')
makedepends=('git' 'python-setuptools')
source=("git+$url.git")
md5sums=('SKIP')

build() {
    cd "$srcdir/$pkgname"
    python -m build --wheel
}

package() {
    cd "$srcdir/$pkgname"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
