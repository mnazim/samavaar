# Flask App Scaffold

Basic flask app scaffold to give me a jump start on projects.

### Features

 - User authentication. Working features include:
   - Login.
   - Register.
   - Change password.
   - All of [Fask-Security](https://pythonhosted.org/Flask-Security/); not all are enabled by default.
 - Stubs for common pages:
   - Dashboard
   - Settings
   - Public Profile

## Roadmap

 - Passwordless login
 - Social login
 - REST API scaffolding
 - React frontend scaffolding
 
## Usage

    git clone git@github.com:mnazim/flask-app-scaffold.git my_app
    cd myapp

...and start modifying as per your need.

## Technical Notes

 - Only PostgreSQL and Flask-SQLAlchemy are supported.
 - All models extend `app.helpers.models.BaseModel`. `BaseModel`, among other things, provides:
   - `id` UUID primary key
   - `created` and `modified` DateTime fields
 - SQL or NoSQL? Why not both?
   - `BaseModel` provides a JSONB field named`data`.
   - Only primary keys, foreign keys, and fields required by third party extensions are stored as separate fields on a model. Everything else going into a JSONB field named `data`.
 - A soft delete mechanism, handled using a Boolean field named `is_trashed`.
   -  `delete()` method only flips `is_trashed` field.

## Screenshots

#### Root page
![Root](http://i.imgur.com/sA1eceh.png)

#### Register
![Register](http://i.imgur.com/0Vyk3Eb.png)

#### Login
![Login](http://i.imgur.com/lQAAvBf.png)

#### Dashboard
![Dashboard](http://i.imgur.com/M3rTB74.png)

#### Settings
![Settings](http://i.imgur.com/nImLB0I.png)

#### Change Password
![Change Password](http://i.imgur.com/oo8ZJwM.png)
