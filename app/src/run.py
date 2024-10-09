import os, sys

from libs.flask_app import create_app, Environment
from libs import str2bool

APP_NAME                  = str(os.environ['APPLICATION_NAME'])
APP_ENV                   = str(os.environ['APPLICATION_ENVIRONMENT'])
APP_USE_DATABASE          = bool(str2bool(os.environ['APPLICATION_USES_DATABASE']))
APP_CREATE_TABLES         = bool(str2bool(os.environ['APPLICATION_INIT_DATABASE']))
APP_HOST                  = str(os.environ['APPLICATION_HOST'])
APP_PORT                  = int(os.environ['APPLICATION_PORT'])

APP_DEBUG                 = bool(str2bool(os.getenv('APPLICATION_ENABLE_DEBUGGER', False)))
APP_DEBUG_PORT            = int(os.getenv('APPLICATION_DEBUGGER_PORT', 5678))
APP_DEBUG_WAIT_FOR_CLIENT = bool(str2bool(os.getenv('APPLICATION_DEBUGGER_WAIT_FOR_CLIENT', False)))

if APP_ENV is Environment.DEVELOPMENT and APP_DEBUG is True:
    import debugpy
    debugpy.listen((APP_HOST, 5678))
    
    if APP_DEBUG_WAIT_FOR_CLIENT is True:
        debugpy.wait_for_client()

app = create_app(
    name         =APP_NAME,
    env          =APP_ENV,
    use_database =APP_USE_DATABASE,
    create_tables=APP_CREATE_TABLES,)

from gevent.pywsgi import WSGIServer
http_server = WSGIServer((APP_HOST, APP_PORT), app)
http_server.serve_forever()
