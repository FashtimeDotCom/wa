#-*- coding:utf-8 -*-
from functools import wraps, partial

class E(object):
    def __init__(self, name, *a, **kw):
        self._name = name
        self._contents = list(a)
        self._attributes = kw

    def __str__(self):
        return '<{0} {1}>{2}</{0}>'.format(
                self._name,
                '' if not self._attributes else ' '.join('{0}="{1}"'.format(k, v) for k, v in self._attributes.iteritems() if v is not None),
                '\n'.join(str(i) for i in self._contents))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        return False
    
    def __le__(self, o):
        self._contents.append(o)
        return o

    def __call__(self, *a, **kw):
        if a:
            self._contents += a
        if kw:
            self._attributes.update(kw)
        return self

#    def __getitem__(self, query):
#        if not query:
#            yield query
#        tag, q = query.split('/', 1)
#        if '@' in tag:
#            tag, where = tag.split('@', 1)
#            if ':' in where:
#                attr, value = where.split(':', 1)
#                for child in self._contents:
#                    if not isinstance(child, E):
#                        continue
#                    if attr in child._attributes and child._attributes[attr] == value:
#                        for i in child[q]:
#                            yield i
#
#    def __setitem__(self, query, value):
#        pass
#
#    def __delitem__(self, query):
#        pass

class SpecialElement(E):
    def __init__(self, open_close, text):
        E.__init__(self, '', text)
        self._open_close = open_close
    
    def __str__(self):
        text = ''.join(self._contents)
        return text.join(self._open_close)

# raw text wrapper
rawtext = partial(SpecialElement, ('', ''))
# HTML tags defines in http://www.htmlquick.com/reference/tags.html
comment = partial(SpecialElement, ('<!-- ', ' -->'))
doctype = partial(SpecialElement, ('<!DOCTYPE ', ' >'))
a = partial(E, 'a')
abbr = partial(E, 'abbr')
acronym = partial(E, 'acronym')
address = partial(E, 'address')
applet = partial(E, 'applet')
area = partial(E, 'area')
b = partial(E, 'b')
base = partial(E, 'base')
basefont = partial(E, 'basefont')
bdo = partial(E, 'bdo')
big = partial(E, 'big')
blockquote = partial(E, 'blockquote')
body = partial(E, 'body')
br = partial(E, 'br')
button = partial(E, 'button')
caption = partial(E, 'caption')
center = partial(E, 'center')
cite = partial(E, 'cite')
code = partial(E, 'code')
col = partial(E, 'col')
colgroup = partial(E, 'colgroup')
dd = partial(E, 'dd')
del_ = partial(E, 'del')
dfn = partial(E, 'dfn')
dir_ = partial(E, 'dir')
div = partial(E, 'div')
dl = partial(E, 'dl')
dt = partial(E, 'dt')
em = partial(E, 'em')
fieldset = partial(E, 'fieldset')
font = partial(E, 'font')
form = partial(E, 'form')
frame = partial(E, 'frame')
frameset = partial(E, 'frameset')
h1 = partial(E, 'h1')
h2 = partial(E, 'h2')
h3 = partial(E, 'h3')
h4 = partial(E, 'h4')
h5 = partial(E, 'h5')
h6 = partial(E, 'h6')
head = partial(E, 'head')
hr = partial(E, 'hr')
html = partial(E, 'html')
i = partial(E, 'i')
iframe = partial(E, 'iframe')
img = partial(E, 'img')
input_ = partial(E, 'input')
ins = partial(E, 'ins')
isindex = partial(E, 'isindex')
kbd = partial(E, 'kbd')
label = partial(E, 'label')
legend = partial(E, 'legend')
li = partial(E, 'li')
link = partial(E, 'link')
map_ = partial(E, 'map')
menu = partial(E, 'menu')
meta = partial(E, 'meta')
noframes = partial(E, 'noframes')
noscript = partial(E, 'noscript')
object_ = partial(E, 'object')
ol = partial(E, 'ol')
optgroup = partial(E, 'optgroup')
option = partial(E, 'option')
p = partial(E, 'p')
param = partial(E, 'param')
pre = partial(E, 'pre')
q = partial(E, 'q')
s = partial(E, 's')
samp = partial(E, 'samp')
script = partial(E, 'script')
select = partial(E, 'select')
small = partial(E, 'small')
span = partial(E, 'span')
strike = partial(E, 'strike')
strong = partial(E, 'strong')
style = partial(E, 'style')
sub = partial(E, 'sub')
sup = partial(E, 'sup')
table = partial(E, 'table')
tbody = partial(E, 'tbody')
td = partial(E, 'td')
textarea = partial(E, 'textarea')
tfoot = partial(E, 'tfoot')
th = partial(E, 'th')
thead = partial(E, 'thead')
title = partial(E, 'title')
tr = partial(E, 'tr')
tt = partial(E, 'tt')
u = partial(E, 'u')
ul = partial(E, 'ul')
var = partial(E, 'var')

__all__ = [i for i in locals() if 'a' <= i[0] <= 'z'] + ['E']

if __name__ == '__main__':
    doc = html(aa='b', cc='d')
    doc(title())
    with doc <= body() as body:
        body(h3('xixi'), new='new', aa='a')
    print doc

    print __all__

