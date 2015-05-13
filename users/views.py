import json
from flask import (Blueprint,
                   render_template,
                   abort,
                   redirect,
                   url_for,
                   request,
                   flash)
from jinja2 import (TemplateNotFound)
import validators
from werkzeug.exceptions import abort
from flask.ext.security import (login_required,
                                current_user)
from helpers.shortcuts import get_object_or_404
from users.models import User
from main import db

from .forms import SettingsForm

users = Blueprint('users', __name__, template_folder='templates')

@users.route('/dashboard')
@login_required
def dashboard():
    flash('This is an informational message.', 'info')
    flash('This is a success message.', 'success')
    flash('This is a warning message.', 'warning')
    flash('This is an error message.', 'error')
    return render_template('dashboard.html')


@users.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    user = User.query.get(current_user.id)
    form = SettingsForm(email=user.email,
                        username=user.username,
                        display_name=user.data.get('display_name', ''),
                        github_name=user.data.get('github', ''),
                        twitter_name=user.data.get('twitter', ''))
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        data = {
            'display_name' : form.display_name.data,
            'github' : form.github_name.data,
            'twitter' : form.twitter_name.data,
        }
        user.update_data(data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('users.dashboard'))
    return render_template('settings.html', form=form)



@users.route('/<slug>')
def profile(slug):
    if validators.uuid(slug):
        account = get_object_or_404(User, User.id == slug)
    elif isinstance(slug, basestring):
        account = get_object_or_404(User, User.username == slug)
    else:
        abort(404)

    return render_template('profile.html', account=account)
