import json
from flask import (Blueprint,
                   render_template,
                   abort,
                   redirect,
                   url_for,
                   request)
from jinja2 import (TemplateNotFound)
from flask.ext.security import (login_required,
                                current_user)
from app.users.models import User
from app import db

from .forms import SettingsForm

users = Blueprint('users', __name__, template_folder='templates')

@users.route('/profile')
@login_required
def private_profile():
    return render_template('profile.html')


@users.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    user = User.query.get(current_user.id)
    form = SettingsForm(email=user.email,
                        display_name=user.data.get('display_name', ''),
                        github_name=user.data.get('github', ''),
                        twitter_name=user.data.get('twitter', ''))
    if form.validate_on_submit():
        user.email = form.email.data
        data = {
            'display_name' : form.display_name.data,
            'github' : form.github_name.data,
            'twitter' : form.twitter_name.data,
        }
        user.update_data(data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('users.private_profile'))
    return render_template('settings.html', form=form)


@users.route('/<id>')
@login_required
def public_profile(id):
    return render_template('public_profile.html')
