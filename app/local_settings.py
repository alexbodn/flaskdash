import os

# *****************************
# Environment specific settings
# *****************************

# DO NOT use "DEBUG = True" in production environments
DEBUG = os.environ.get('DEBUG', True)

# DO NOT use Unsecure Secrets in production environments
# Generate a safe one with:
#     python -c "from __future__ import print_function; import string; import random; print(''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(24)]));"
SECRET_KEY = os.environ.get('SECRET_KEY', 'This is an UNSECURE Secret. CHANGE THIS for production environments.')

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///../app.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)    # Avoids a SQLAlchemy Warning

# Flask-Mail settings
# For smtp.gmail.com to work, you MUST set "Allow less secure apps" to ON in Google Accounts.
# Change it in https://myaccount.google.com/security#connectedapps (near the bottom).
MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
MAIL_PORT = os.environ.get('MAIL_PORT', 587)
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', False)
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', True)
MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'you@gmail.com')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'yourpassword')
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', '"You" <you@gmail.com>')
ADMINS = [
    '"Admin One" <admin1@gmail.com>',
    ]
