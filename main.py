import os
import sys
from flask import (Flask,
                   render_template,
                   jsonify,
                   redirect,
                   url_for)

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import (Security,
                                SQLAlchemyUserDatastore,
                                login_required,
                                current_user)
from flask.ext.migrate import (Migrate, MigrateCommand)


app = Flask('flask-app-scaffold')
app.config.from_object('settings')

db = SQLAlchemy(app)

from users.views import users as users_bp
app.register_blueprint(users_bp)
from social.apps.flask_app.routes import social_auth
app.register_blueprint(social_auth)


def get_user_datastore():
    """ We encapsulate this in a function to avoid cyclic import """
    from users.models import User, Role
    return SQLAlchemyUserDatastore(db, User, Role)

security = Security(app, get_user_datastore())


def install_secret_key(app, filename='secret_key'):
    """Configure the SECRET_KEY from a file
    in the instance directory.

    If the file does not exist, print instructions
    to create it from a shell with a random key,
    then exit.
    """
    filename = os.path.join(app.instance_path, filename)

    try:
        app.config['SECRET_KEY'] = open(filename, 'rb').read()
    except IOError:
        print('Error: No secret key. Create it with:')
        full_path = os.path.dirname(filename)
        if not os.path.isdir(full_path):
            print('mkdir -p {filename}'.format(filename=full_path))
        print('head -c 24 /dev/urandom > {filename}'.format(filename=filename))
        sys.exit(1)

if not app.config['DEBUG']:
    install_secret_key(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def index():
    if current_user.is_authenticated():
        return redirect(url_for('users.dashboard'))
    return render_template('home.html');
