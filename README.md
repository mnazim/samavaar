# Samavaar

Samavar is a minimal flask application scaffold to give **me** a jump start on Flask projects. *No part of this project is supposed to be used as is, for long*. I use samavaar as starting point and it evolves with the project over time.

### Features
 - User authentication. Working features include:
   - Login.
   - Register.
   - Change password
   - All of [Fask-Security](https://pythonhosted.org/Flask-Security/); not all are enabled by default.
 - Stubs for common pages:
   - Dashboard
   - Settings
   - Public Profile
 - Basic Gravatar integration

## Roadmap (in no particular order)
 - Simple notifications app
   - Plugable notification delivery via email, text messages, etc. 
 - Passwordless login.
 - Social login.
 - REST API scaffolding.
 - React frontend scaffolding.
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
   - Only primary keys, foreign keys, and fields required by third party extensions are stored as separate fields on a model. Everything else going into a JSONB field.
   - `is_disabled` flag on records controls whether the record appears in the query results or not. `BaseModel.disable` and `BaseModel.enable` are helper methods to flip `is_disabled`. Implementing semantics around disabled/enabled states are left for client class to implement.
   - Samavaar has a flatter directory structure than usually suggested for flask apps, for instance, in this [Large App Howto](https://github.com/mitsuhiko/flask/wiki/Large-app-how-to).

## Screenshots

Looks are not really the point of the project. You would most definitely be coding your own front end templates. Following screenshots are purely for demonstrational purposes.

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
