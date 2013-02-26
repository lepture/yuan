DEBUG = False
TESTING = False

#: site
SITE_TITLE = 'Yuan'
SITE_URL = '/'
SITE_FEED = ''
SITE_LOGO = ''
SITE_FOOTER = ''
SITE_VERSION = '20130220'
SITE_GA = None

#: session
SESSION_COOKIE_NAME = 'yuan'
#SESSION_COOKIE_SECURE = True
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30

#: account
PASSWORD_SECRET = 'password-secret'
GRAVATAR_BASE_URL = 'http://www.gravatar.com/avatar/'
GRAVATAR_EXTRA = ''

#: sqlalchemy
# SQLALCHEMY_POOL_SIZE = 100
# SQLALCHEMY_POOL_TIMEOUT = 10
# SQLALCHEMY_POOL_RECYCEL = 3600

#: cache
CACHE_TYPE = 'simple'
#CACHE_REDIS_HOST
#CACHE_REDIS_PORT
#CACHE_REDIS_PASSWORD

#: file storage
WWW_ROOT = 'data'
MIRROR_URL = 'http://spmjs.org/repository/'
