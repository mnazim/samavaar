from flask.ext.wtf import Form
import wtforms
from wtforms.validators import DataRequired
from main import app

class SettingsForm(Form):
    email = wtforms.TextField(validators=[DataRequired()])
    username = wtforms.TextField(
        description='<em>{}<span class="url_username">username</span></em> will become your url'.format(app.config['APP']['base_url'])
    )
    display_name = wtforms.TextField()
    github_name = wtforms.TextField()
    twitter_name = wtforms.TextField()
