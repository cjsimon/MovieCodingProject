from . import configuration as config
from argparse import ArgumentParser
import os, sys

parser = ArgumentParser(description='MovieManager WebApp')

parser.add_argument(
    '-d', '--daemon', '--daemonize',
    help='Use this flag to daemonize the process',
    action='store_true')

parser.add_argument(
    '-e', '--env', '--environment',
    help=' '.join([
        'Environment to use when launching the WebApp.'
        'If unspecified, the APPLICATION_ENVIRONMENT envvar is fetched and used']),
    type=config.Environment,
    required=True,
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
