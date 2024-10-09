# https://nickjanetakis.com/blog/configuring-gunicorn-for-development-and-production-with-env-variables

import os
import multiprocessing

from libs import str2bool

#APP_HOST         = str(os.environ['APPLICATION_HOST'])
#APP_PORT         = int(os.environ['APPLICATION_PORT'])

APP_CONCURRENCY   = int(os.getenv('GUNICORN_CONCURRENCY', multiprocessing.cpu_count() * 2))
APP_MAX_THREADS   = int(os.getenv('GUNICORN_MAX_THREADS', 1))
APP_HOT_RELOAD    = bool(str2bool(os.getenv('GUNICORN_HOT_RELOAD', False)))

#host             = APP_HOST
#port             = APP_PORT

#bind             = '%(host)s:%(port)s' % { 'host': APP_HOST, 'port': APP_PORT }
accesslog         = '-'
access_log_format = "%(h)s %(l)s %(u)s %(t)s '%(r)s' %(s)s %(b)s '%(f)s' '%(a)s' in %(D)sµs"

workers           = APP_CONCURRENCY
threads           = APP_MAX_THREADS

reload            = APP_HOT_RELOAD
