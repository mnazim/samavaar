from helpers.models import BaseModel
from app.users.models import User


class Notification(BaseModel):
    __tablename__ = 'users_notifications'
    user = db.relationship(User, backref=db.backref('notifications', lazy='dynamic'))
    is_read = db.Column(db.BooleanField, default=False)

    def __init__(self, **kwargs):
        # No point creating an already read notification
        if 'is_read' in kwargs: kwargs.pop('is_read')
        self.is_read = False
        self.user = kwargs.pop('user')
        self.data = kwargs

    @property
    def is_unread(self):
        return not self.is_read

    def mark_unread(self):
        self.is_read = False

    def mark_read(self):
        self.is_read = True

    def as_html(self):
        pass

    def as_json(self):
        pass
