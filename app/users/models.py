import urllib
import hashlib
from flask.ext.security import (UserMixin,
                                RoleMixin)
from sqlalchemy_utils import (IPAddressType,
                              UUIDType)
from app import db

from app.helpers.models import BaseModel


roles_users = db.Table(
    'users_roles',
    db.Column('user_id', UUIDType, db.ForeignKey('users.id')),
    db.Column('role_id', UUIDType, db.ForeignKey('roles.id')),
)

class Role(BaseModel, RoleMixin):
    __tablename__ = 'roles'

    def __init__(self, **kwargs):
        self.data = dict(**kwargs)


class User(BaseModel, UserMixin):
    __tablename__ = 'users'
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    last_login_at = db.Column(db.DateTime)
    current_login_at = db.Column(db.DateTime)
    last_login_ip = db.Column(IPAddressType)
    current_login_ip = db.Column(IPAddressType)
    login_count = db.Column(db.Integer, default=0)

    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


    def __init__(self, **kwargs):
        from pprint import pprint
        pprint(kwargs)
        self.email = kwargs.pop('email')
        self.password = kwargs.pop('password')
        self.active = kwargs.pop('active')
        self.roles = kwargs.pop('roles')
        self.data = dict(**kwargs)


    def __repr__(self):
        return self.display_name

    @property
    def display_name(self):
        return self.data.get('display_name', self.email)


    def gravatar(self, size='200'):
        gravatar_url = "http://www.gravatar.com/avatar/{}?".format(hashlib.md5(self.email.lower()).hexdigest())
        gravatar_url += urllib.urlencode({'d':'identicon', 's':size})
        return gravatar_url
