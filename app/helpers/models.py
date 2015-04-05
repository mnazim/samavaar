import uuid
from datetime import datetime
from sqlalchemy.dialects.postgres import JSONB
from sqlalchemy_utils import JSONType
from sqlalchemy_utils import UUIDType

from app import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(UUIDType,
                   primary_key=True,
                   default=str(uuid.uuid4()))

    data = db.Column(JSONB)

    is_trashed = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime,
                        default=datetime.utcnow)
    modified = db.Column(db.DateTime,
                         onupdate=datetime.utcnow)


    def __init__(self, **kwargs):
        """ Client model must provide __init__.

        Simple User model example:

        class User(BaseModel):
            __tablename__ = 'users'
            email = db.Column(db.String(255), unique=True)
            password = db.Column(db.String(255))
            active = db.Column(db.Boolean)

            def __init__(self, **kwargs):
                self.email = kwargs.pop('email')
                self.password = kwargs.pop('password')
                self.active = kwargs.pop('active')

                # self.data expects valid JSON data;
                # it is developer's responsibility to provide
                # transparent serialization of complex object,
                # before saving to database.
                self.data = dict(**kwargs)
        """
        pass

    def _trash(self):
        self.is_trashed = True
        db.session.add(self)
        db.session.commit()

    def delete(self, *args, **kwargs):
        self._trash()

    def destroy(self, *args, **kwargs):
        super(User, self).delete(*args, **kwargs)

    def update_data(self, data):
        assert(isinstance(data, dict))

        _d = self.data.copy()
        _d.update(data)
        self.data = _d
