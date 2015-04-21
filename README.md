# Samavaar

Samavar is a minimal flask application scaffold to give **me** a jump start on projects.

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
 - Basic Gravatar integration.

## Roadmap (in no particular order)
 - Simple notifications app
 - Passwordless login
 - Social login
 - REST API scaffolding
 - React frontend scaffolding
 - Test suite and code coverage.
 
## Usage

    git clone git@github.com:mnazim/samavaar.git myapp
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
   - `is_disabled` flag on rows controls whether they appear in the query results or not. `BaseModel.disable` and `BaseModel.enable` are helper methods to flip `is_disabled` Disable and enable semantics are client class to implement.

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
