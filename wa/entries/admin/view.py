
import os

from flask.views import MethodView


from flask import Blueprint, redirect, url_for, make_response


from flask import render_template

from wa.forms import LoginForm

from flask.ext.user import current_user, login_required, UserManager, UserMixin, SQLAlchemyAdapter

HERE = os.path.dirname(__file__)

admin = Blueprint('admin', __name__,
        static_folder='./static',
        template_folder='./templates')

#def render_template(filename, **kw):
#    content = open(os.path.join(filename)).read()
#    return make_response(content.format(**kw))



# The '/' page is accessible to anyone
@admin.route('/')
def home_page():
    if current_user.is_authenticated():
#        return redirect(url_for('admin.profile_page'))
#        return make_response(open(os.path.join(HERE, 'templates/index.html')).read())
        return render_template('index.html')
#        return render_template(os.path.join(HERE, 'templates/index.html'),
#                               controllers_js=url_for('admin.static', filename='js/controllers.js'))
    return redirect(url_for('user.login'))
