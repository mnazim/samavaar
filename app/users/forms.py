from flask.ext.wtf import Form
import wtforms
from wtforms.validators import DataRequired

class SettingsForm(Form):
    email = wtforms.TextField(validators=[DataRequired()])
    display_name = wtforms.TextField()
    github_name = wtforms.TextField()
    twitter_name = wtforms.TextField()

