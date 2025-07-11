import os

# Superset specific config
# ROW_LIMIT = 5000
ROW_LIMIT = 50000000
SAMPLES_ROW_LIMIT = 50000000
FILTER_SELECT_ROW_LIMIT = 50000000
QUERY_SEARCH_LIMIT = 50000000
SQL_MAX_ROW = 500000000
DISPLAY_MAX_ROW = 50000000
DEFAULT_SQLLAB_LIMIT = 50000000

# Flask App Builder configuration
# Your App secret key will be used for securely signing the session cookie
# and encrypting sensitive information on the database
# Make sure you are changing this key for your deployment with a strong key.
# Alternatively you can set it with `SUPERSET_SECRET_KEY` environment variable.
# You MUST set this for production environments or the server will refuse
# to start and you will see an error in the logs accordingly.
SECRET_KEY = 'iGJFOh24XJ3rFldSpvGXDHOcmMlATrJfdtjoJnBY6J9A6u6C9UPUDcFq'

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
# The check_same_thread=false property ensures the sqlite client does not attempt
# to enforce single-threaded access, which may be problematic in some edge cases
PWD = os.getcwd()
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(PWD,'superset.db')+'?check_same_thread=false'
PREVENT_UNSAFE_DB_CONNECTIONS = False
TALISMAN_ENABLED= False

# Flask-WTF flag for CSRF
CSRF_ENABLED = False
WTF_CSRF_ENABLED = False

# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''