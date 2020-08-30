from nadine.settings.base import *
#from socket import *
import os
import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

PRODUCTION = False
DEBUG = True

# Admins
ADMINS = (
    ('admin', 'admin@fake.com'),
)
MANAGERS = ADMINS
SERVER_EMAIL = 'nadine@officenomads.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nadinedb',
        'USER': 'postgres',
        'PASSWORD': 'somepassword',
        'HOST': 'db',
        'PORT': 5432,
     }
}

COUNTRY = "AR"
TIME_ZONE = "America/Argentina/Buenos_Aires"

STATIC_ROOT = "/webapp/static"
MEDIA_ROOT = "/webapp/media"

# CACHE_BACKEND = 'dummy:///'
CACHE_BACKEND = 'locmem:///'

# Make this unique, and don't share it with anybody.
# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = 'ZZZ'

GOOGLE_ANALYTICS_ID = 'YOUR-GOOGLE-CODE'

MAILCHIMP_API_KEY = "goMonkeygo"
MAILCHIMP_NEWSLETTER_KEY = "melikekey"
MAILCHIMP_WEBHOOK_KEY = "hookedonhooks"

# Xero Integration Settings
# Generate an RSA key and register it with Xero as a private application.
# openssl genrsa -out privatekey.pem 1024
# openssl req -new -x509 -key privatekey.pem -out publickey.cer -days 1825
# openssl pkcs12 -export -out public_privatekey.pfx -inkey privatekey.pem -in publickey.cer
XERO_CONSUMER_KEY = "secretkey"
XERO_PRIVATE_KEY = "/keys/privatekey.pem"

SLACK_API_TOKEN = "your token"
SLACK_TEAM_URL = "https://nadine.slack.com/"

DISCOURSE_BASE_URL = 'http://your-discourse-site.com'
DISCOURSE_SSO_SECRET = 'paste_your_secret_here'

ARPWATCH_SNMP_SERVER = '192.168.1.1'
ARPWATCH_SNMP_COMMUNITY = 'yourcommunitystring'
ARPWATCH_NETWORK_PREFIX = '192.168.'

DEFAULT_FROM_EMAIL = "nadine@fake.com"
EMAIL_HOST = "fakesmtp"
#EMAIL_HOST_PASSWORD = "password"
#EMAIL_HOST_USER = "username"
#EMAIL_USE_TLS = True
EMAIL_PORT = 25
#EMAIL_SUBJECT_PREFIX = "[COWORKING] "  # or None if you want no subject prefix

# Mailgun Settings
#MAILGUN_API_KEY = "4d640632-e16915731"
#MAILGUN_DOMAIN = "sandbox59b58afa8e5d4d83b180abe02efa6d2d1.mailgun.org"
#MAILGUN_DEBUG = True

TEAM_EMAIL_ADDRESS = "team@fake.com"
TEAM_MEMBERSHIP_PLAN = "ON Team"

#import netifaces as ni
#ni.ifaddresses('eth0')
#ip = ni.ifaddresses('eth0')[AF_INET][0]['addr']
#ALLOWED_HOSTS = [ip, 'localhost', '127.0.0.1']
ALLOWED_HOSTS = ['*']