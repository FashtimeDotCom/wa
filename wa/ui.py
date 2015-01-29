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


def panel_table(title, data, head_map, other_component):
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
        ),
        other_component,
    )


def pagination(total, current, href_func, near=1):
    lis = []
    bgn, end = 1, total
    for i in xrange(total):
        page_num = i + 1
        if page_num == current:
            curr_li = h.li(klass='active')
        else:
            curr_li = h.li()
        if page_num == bgn or page_num == end:
            lis.append(curr_li(h.a(str(page_num), href=href_func(page_num))))
        elif abs(page_num - current) <= near:
            lis.append(curr_li(h.a(str(page_num), href=href_func(page_num))))
        elif abs(page_num - current) > near and (abs(page_num - bgn) == 1 or abs(page_num - end) == 1):
            lis.append(curr_li(h.a('...'), klass='disabled'))
    return h.nav(
        h.ul(
            *lis,
            klass='pagination'
        ),
        h.form(
            h.rawtext('跳转到：'),
            h.input_(
                type='text',
                name='page',
                placeholder=str(current),
            ),
            h.input_(
                type='submit',
                value='确定',
            ),
            method='get',
        ),
    )


container = partial(build, 'container')
container_fluid = partial(build, 'container-fluid')
row = partial(build, 'row')
col = partial(build, 'col')
main = partial(build, 'main')
sidebar = partial(build, 'sidebar')
footer = partial(build, 'footer')
navbar = partial(build, 'navbar')