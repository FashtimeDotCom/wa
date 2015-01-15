

from bottle import Bottle

from .html import *

admin = Bottle()

@admin.route('/')
def test():
    with html() as doc:
        title('test')
        with body():
            adiv = div()
            adiv.h1('Hello, world! Admin')
    return doc


def init():
    return admin