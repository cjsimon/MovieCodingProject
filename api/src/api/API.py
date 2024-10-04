import http.client
import requests

class API:
    def __init__(self, endpoints):
        self.endpoints = endpoints
                
    def exec(endpoint, connection=None, url=None, route=None, params=None, method=None):
        """
        Execute a given parameterized endpoint query and return the client connection for processing
        """
        
        validate_params(endpoint.params)
        
        url = endpoint.url if url is None else url
        route = '%(url)s%(route)s?%(params)s' % {
            route:  endpoint.route if route is None else route,
            params: construct_urlparams(endpoint.params if params is None else params),
        }
        method = endpoint.method if method is None else method
        
        connection = http.client.HTTPSConnection() if connection is None else connection
        connection.request(method, route, None)
        
        return connection
    
    def construct_urlparams(params):
        param_string = ''
        
        for param in params(depth=1):
            if param.value is None or not hasattr(param, 'value'):
                continue
            
            param_string += '%(param)s=%(value)s&' % {
                param: param.get_key(),
                value: param.value,
            }
        
        return param_string[:-1] # Omit the last extra &
    
    def validate_params(params):
        for param in params(depth=1):
            resolve_options_shorthand(param)
            validate_value(param)
    
    def resolve_options_shorthands(param):
        resolve_options_str_shorthands(param)
    
    def resolve_options_str_shorthands(param):
        """
        Resolve {options: [...]} shorthand for {type: str} to expected lambda.
        
        From:   {options: ['sample', 'valid', 'values']}
        To:     {options: lambda {value}: ({value} in {options})}
        """
        
        if param.Type is str and param.options is list:
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
