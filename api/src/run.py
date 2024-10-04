import os, sys

from flask_app import create_app, Environment
from flask_app.libs import str2bool

APP_NAME          = os.environ['APPLICATION_NAME']
APP_ENV           = os.environ['APPLICATION_ENVIRONMENT']
APP_USE_DATABASE  = str2bool(os.environ['APPLICATION_USES_DATABASE'])
APP_CREATE_TABLES = str2bool(os.environ['APPLICATION_INIT_DATABASE'])
APP_HOST          = os.environ['APPLICATION_HOST']
APP_PORT          = os.environ['APPLICATION_PORT']

app = create_app(
    name         =APP_NAME,
    env          =APP_ENV,
    use_database =APP_USE_DATABASE,
    create_tables=APP_CREATE_TABLES,)

if APP_ENV == Environment.TESTING or APP_ENV == Environment.DEVELOPMENT:
    app.run(
        host=APP_HOST,
        port=APP_PORT,
        debug=True,)

if APP_ENV == Environment.STAGING or APP_ENV == Environment.PRODUCTION:
    from gevent.pywsgi import WSGIServer
    app = WSGIServer((os.environ['APPLICATION_HOST'], os.environ['APPLICATION_PORT']), app)
    app.serve_forever()
