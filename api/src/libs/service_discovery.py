class ServiceDiscovery:
    """
    Helper class to retrieve service endpoints
    
    TODO: Determine how to discover hosts of other services within their own kuernetes clusters
    """
    
    @staticmethod
    def getApiHost():
        return 'host.containers.internal:4321'
        pass
    
    @staticmethod
    def getAppHost():
        return 'host.containers.internal:80'
        pass
