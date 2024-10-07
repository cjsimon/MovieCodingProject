import os, sys

from libs.flask_app import create_app, Environment
from libs import str2bool

APP_NAME          = os.environ['APPLICATION_NAME']
APP_ENV           = os.environ['APPLICATION_ENVIRONMENT']
APP_USE_DATABASE  = str2bool(os.environ['APPLICATION_USES_DATABASE'])
APP_CREATE_TABLES = str2bool(os.environ['APPLICATION_INIT_DATABASE'])
APP_HOST          = os.environ['APPLICATION_HOST']
APP_PORT          = int(os.environ['APPLICATION_PORT'])

app = create_app(
    name         =APP_NAME,
    env          =APP_ENV,
    use_database =APP_USE_DATABASE,
    create_tables=APP_CREATE_TABLES,)

from gevent.pywsgi import WSGIServer
http_server = WSGIServer((APP_HOST, APP_PORT), app)
http_server.serve_forever()
