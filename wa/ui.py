# -*- coding:utf-8 -*-

from functools import partial

from . import html as h


def page(*a):
    return h.rawtext('')(h.doctype('html'), h.html(lang='zh-cn')(*a))


def build(ui_type, *a, **kw):
    if 'klass' in kw:
        kw['klass'] = ' '.join((ui_type, kw['klass']))
    else:
        kw['klass'] = ui_type
    return h.div(*a, **kw)


def panel(title, *a, **kw):
    return build("panel panel-default")(
        build("panel-heading")(title),
        build("panel-body")(*a, **kw)
    )


def panel_table(title, data, head_map):
    # make head
    thead = h.thead()(
        h.tr()(
            *(h.th(v) for v in head_map.itervalues())
        )
    )

    # make tbody
    tbody = h.tbody()
    for row in data:
        tr = h.tr()
        for k in head_map.iterkeys():
            tr(h.td(getattr(row, k)))
        tbody(tr)

    return build("panel panel-default")(
        build("panel-heading")(title),
        h.table(
            thead,
            tbody,
            klass='table'
        )
    )


container = partial(build, 'container')
container_fluid = partial(build, 'container-fluid')
row = partial(build, 'row')
col = partial(build, 'col')
main = partial(build, 'main')
sidebar = partial(build, 'sidebar')
footer = partial(build, 'footer')
navbar = partial(build, 'navbar')