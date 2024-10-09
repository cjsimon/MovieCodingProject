import http.client
import requests

class API:
    def __init__(self, endpoints):
        self.endpoints = endpoints
    
    def exec(endpoint, connection=None, host=None, route=None, params=None, method=None):
        """
        Execute a given parameterized endpoint query and return the client connection for processing
        """
        
        params = process_params(params) if params is not None else process_params(endpoint.params) if endpoint.params is not None else None
        
        host = host if host is not None else endpoint.host if endpoint.host is not None else self.host
        route = '%(route)s?%(params)s' % {
            route:  route if route is not None else endpoint.route,
            params: construct_urlparams(params),
        }
        method = method if method is not None else endpoint.method
        
        connection = connection if connection is not None else http.client.HTTPSConnection(host)
        connection.request(method, route, None)
        
        return connection
    
    def construct_urlparams(params):
        """
        Construct a urlparams string given a set of endpoint params
        """
        
        params_string = ''
        
        for param in params(depth=1):
            param_string = construct_urlparam(param)
            
            if param_string:
                params_string += param_string
        
        return params_string[:-1] # Omit the last extra &
    
    def construct_urlparam(param):
        """
        Construct a urlparam string for a given endpoint param
        """
        
        for param in params(depth=1):
            if param.value is None or not hasattr(param, 'value'):
                return False
            
            return '%(param)s=%(value)s&' % {
                param: param.get_key(),
                value: param.value,
            }
    
    def process_params(params, construct_urlparams=True):
        """
        Process params by resolving any options shorthands that may exist, and by validaing them.
        Since this requires iterating over the params, optionally the construction of the url params
        can occur here as well to same an otherwise addtional iteration over each of the params from
        a seperate construct_urlparams call
        """
        
        if construct_urlparams:
            params_string = ''
        
        for param in params(depth=1):
            resolve_options_shorthand(param)
            validate_value(param)
            
            if construct_urlparams:
                construct_urlparam(param)
        
        if construct_urlparams:
            params_string = params_string[:-1] # Omit the last extra &
    
    def resolve_options_shorthands(param):
        """
        Some param options shorthands exist for specific types.
        Check and process any potential shorthands that may exists for those types
        """
        
        if param.Type is str:
            resolve_options_str_shorthand(param)
    
    def resolve_options_str_shorthand(param):
        """
        Resolve {options: [...]} shorthand for {type: str} to expected lambda.
        
        From:   {options: ['sample', 'valid', 'values']}
        To:     {options: lambda {value}: ({value} in {options})}
        """
        
        if param.options is list:
            param.options = lambda s: s in param.options
    
    def validate_value(param):
        """
        Validate a given param against various param.value requirements
        """
        
        validate_value_required(param)
        validate_value_type(param)
        validate_value_option_requirements(param)
    
    def validate_value_required(param):
        """
        Verify that if a value is required, that it is not None
        """
        
        if param.value is None and param.required:
            raise ValueError('Required param %(param_name)s value expected to be set' % {param_name: param.get_key()})
        
    def validate_value_type(param):
        """
        Verify that the param.value is of its expected type
        
        Note: Subclasses that inherit the base type are valid
        """
        
        if not isinstance(param.value, param.Type):
            raise ValueError('Param %(param_name)s value must be a kind of {param.Type}' % {param_name: param.get_key()})
    
    def validate_value_option_requirements(param):
        """
        Verify that the param.value satisfies its option requirements
        """
        
        if not param.options(param.value):
            raise ValueError('Param %(param_name)s value does not meet its option requirements' % {param_name: param.get_key()})
