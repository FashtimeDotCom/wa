# -*- coding: utf-8 -*-


import re

from flask import Markup


from flask.ext.wtf import Form
from wtforms import BooleanField, TextField, validators, \
             PasswordField, IntegerField, TextAreaField, SelectField, FileField
from flask.ext.wtf.html5 import EmailField


REGEX_CHINA_PHONE = r'^0?(13[0-9]|15[012356789]|18[0236789]|14[57])[0-9]{8}$'


class CommitForm(Form):

    name = TextField(u'姓名')
    phone = TextField(u'手机号码', [validators.Required(),
                  validators.Length(min=11, max=12),
                  validators.Regexp(regex=re.compile(REGEX_CHINA_PHONE), message=u"电话号码格式错误")])
    address = TextField(u'申请地址')
    grade = TextField(u'学历')
    age = TextField(u'年龄')
    idcard = TextField(u'身份证号码')
    sex = TextField(u'性别')
    addr_belong = TextField(u'地址归属')
    qudao = TextField(u'qudao')

    def render_html(self):

        html = u'申请人信息： \n\n'
        html += u'------------------------------------------\n'
        html += u'姓名：%s' % self.name.data
        html += u'\n联系电话：%s' % self.phone.data
        html += u'\n身份证号码：%s' % self.idcard.data
        html += u'\n地址归属地：%s' % self.addr_belong.data
        html += u'\n地址：%s' % self.address.data
        html += u'\n渠道：%s' % self.qudao.data
        html += u'\n性别：%s' % self.sex.data
        html += u'\n学历：%s' % self.grade.data
        html += u'\n年龄：%s' % self.age.data
        html += u'\n------------------------------------------\n'
        return html


CATEGORYS = (

)

class LoginForm(Form):

    user_name = TextField(u'用户名')
    password  = TextField(u'密码')

class NewsForm(Form):

    category_id = TextField(u'新闻分类')
    title = TextField(u'标题')
    title_code = TextField(u'标题的编码')
    content = TextField(u'内容')
    is_hide = TextField(u'是否隐藏')
    author = TextField(u'编者')

class NewsEditForm(Form):

    id = TextField(u'新闻ID')
    category_id = TextField(u'新闻分类')
    title = TextField(u'标题')
    title_code = TextField(u'标题的编码')
    content = TextField(u'内容')
    is_hide = BooleanField(u'是否隐藏')
    author = TextField(u'编者')


class NewsCategoryForm(Form):

    name = TextField(u'姓名')
    phone = TextField(u'手机号码', [validators.Required(),
                  validators.Length(min=11, max=12),
                  validators.Regexp(regex=re.compile(REGEX_CHINA_PHONE), message=u"电话号码格式错误")])
    address = TextField(u'申请地址')
    grade = TextField(u'学历')
    age = TextField(u'年龄')
    idcard = TextField(u'身份证号码')
    sex = TextField(u'性别')
    addr_belong = TextField(u'地址归属')
    qudao = TextField(u'qudao')



class AdvertiseForm(Form):
    name = TextField(label=u'图片名称', validators=[validators.InputRequired(), validators.Length(min=1, max=100)])
    image_target_url = TextField(label=u'目标链接', validators=[validators.InputRequired(), validators.url()])
    image_uri = TextField(label=u'上传图片', validators=[validators.InputRequired()])


class UploadForm(Form):
    target_url = TextField(u'目标链接')
    is_hidden = BooleanField(u'是否隐藏')
    file = FileField(u'文件上传')

class SiteConfigForm(Form):
    title = TextField(u'标题')
    file = FileField(u'上传Logo')
    foot_style = TextAreaField(u'底部样式')
    keyword = TextField(u'SEO关键词')
    description = TextAreaField(u'SEO描述')

class CategoryForm(Form):
    name = TextField(u'名称', [validators.Required(message=u'名称不能为空')])
    code = TextField(u'编码', [validators.Required(message=u'编码不能为空')])

class WidgetForm(Form):
    title = TextField(u'标题', [validators.Required(message=u'标题不能为空')])
    content = TextField(u'内容', [validators.Required(message=u'内容不能为空')])
    position = TextField(u'位置')
    is_hidden = BooleanField(u'是否隐藏')
