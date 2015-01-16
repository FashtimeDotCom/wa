# -*- coding:utf-8 -*-

from functools import partial

from . import html as h

def page(*a):
    return h.rawtext('')(h.doctype('html'), h.html(lang='zh-cn')(*a))

def build(ui_type, *a, **kw):
    if 'class' in kw:
        kw['class'] = ' '.join((ui_type, kw['class']))
    else:
        kw['class'] = ui_type
    return h.div(*a, **kw)

container = partial(build, 'container')
container_fluid = partial(build, 'container-fluid')
row = partial(build, 'row')
col = partial(build, 'col')
main = partial(build, 'main')
sidebar = partial(build, 'sidebar')
footer = partial(build, 'footer')