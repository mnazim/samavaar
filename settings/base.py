import os

def app_root(*args):
    path = approot = os.path.abspath(
        os.path.dirname(__file__, '..')
    )
    if len(args) > 0:
        path = os.path.join(approot, *args)
    return path


DEBUG = False
SECRET_KEY = 'asDASD#@$Sdfl = sdfy9s8dn; @#$gh76sftW423 jg76sdvSDfsi7-df623442'
DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 8
SECURITY_URL_PREFIX = '/accounts'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = 'A.!/!''[]~)_\|4Aa%Sf|D|{}:""^^hADu&ScGnJm*kiTsh@#jYi+-U$^@7%s4@'
SECURITY_REGISTERABLE = True
SECURITY_TRACKABLE = True
SECURITY_CHANGEABLE = True
SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
SECURITY_DEFAULT_REMEMBER_ME = True
SECURITY_SEND_REGISTER_EMAIL = False




DEFAULT_AVATAR_PATH = '/static/images/defaultavatar.png'
