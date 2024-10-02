from . import configuration as config
from argparse import ArgumentParser
import os, sys

parser = ArgumentParser(description='MovieManager API')

parser.add_argument(
    '-d', '--daemon', '--daemonize',
    help='Use this flag to daemonize the process',
    action='store_true')

parser.add_argument(
    '-e', '--env', '--environment',
    help=' '.join([
        'Environment to use when launching the API.'
        'If unspecified, the APPLICATION_ENVIRONMENT envvar is fetched and used']),
    type=config.Environment,
    required=False, # Should be True, but even with a default set,
                    # an error occurs if a value isn't explicitly supplied.
                    # Luckly, the type enforcement catches the case of the
                    # envvar not being defined, so this should be okay atm
    default=os.environ.get('APPLICATION_ENVIRONMENT'))

parser.add_argument(
    '-a', '--host', '--address',
    help=' '.join([
        'Host address to broadcast the server on',
        'If unspecified, the APPLICATION_HOST envvar is fetched and used']),
    type=str,
    required=False,
    default=os.environ.get('APPLICATION_HOST'))

parser.add_argument(
    '-p', '--port',
    help=' '.join([
        'Port to broadcast the server on',
        'If unspecified, the APPLICATION_PORT envvar is fetched and used']),
    type=int,
    required=False,
    default=os.environ.get('APPLICATION_PORT'))

parser.add_argument(
    '--database', '--use-database',
    help='Use this flag to instantiate a database connection to the specified database',
    action='store_true')

parser.add_argument(
    '--dbhost',
    help=' '.join([
        'The database host to establish a connection to',
        'If unspecified, the DATABASE_HOST envvar is fetched and used']),
    type=str,
    required=False,
    default=os.environ.get('DATABASE_HOST'))

parser.add_argument(
    '--dbport',
    help=' '.join([
        'The database port to establish a connection to',
        'If unspecified, the DATABASE_PORT envvar is fetched and used']),
    type=str,
    required=False,
    default=os.environ.get('DATABASE_PORT'))

parser.add_argument(
    '--dbname',
    help=' '.join([
        'The database name to use to after a connection is established with the database host',
        'If unspecified, the DATABASE_NAME envvar is fetched and used']),
    type=str,
    required=False,
    default=os.environ.get('DATABASE_NAME'))

parser.add_argument(
    '--dbuser',
    help=' '.join([
        'The database username for login',
        'If unspecified, the DATABASE_USERNAME envvar is fetched and used']),
    type=str,
    required=False,
    default=os.environ.get('DATABASE_USERNAME'))

parser.add_argument(
    '--dbpass',
    help=' '.join([
        'The database user password',
        'If unspecified, the DATABASE_PASSWORD envvar is fetched and used']),
    type=str,
    required=False,
    default=os.environ.get('DATABASE_PASSWORD'))

parser.add_argument(
    '-c', '--create', '--create_tables',
    help='Use this flag to create the database tables if they don\'t already exist',
    action='store_true')

def parse_args():
    """
    Parse arguments from the command
    """
    return parser.parse_args()

def verify_args(args):
    """
    Custom rules to verify a set of arguments against a specific rule-set
    This is a fallback if argparse does not catch an error that we want to
    """
    try:
        # Try to select the arg env specified
        # to determine if it is a valid Environment
        config.Environment(args.env)
    except: #(AttributeError, KeyError, ValueError): # Catch any error, not just expected errors
        environment_names = [(env.value) for env in config.Environment]
        parser.print_help()
        sys.exit(
            '\n%s is not a valid configuration!\nPossible values are %s'
            % (args.env, environment_names))

def get_args():
    """
    Parse and verify CLI arguments,
    and return them for use if valid
    """
    args = parse_args()
    
    verify_args(args)
    
    return args
