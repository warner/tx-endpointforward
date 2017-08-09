from twisted.internet import protocol
from twisted.protocols import portforward

class EndpointProxyServer(portforward.ProxyServer):
    # we modify connectionMade to use endpoints.clientFromString instead of
    # reactor.connectTCP

    def connectionMade(self):
        self.transport.pauseProducing()
        client = self.clientProtocolFactory()
        client.setServer(self)
        self.factory.outbound_endpoint.connect(client)

class EndpointProxyFactory(protocol.Factory):
    protocol = EndpointProxyServer

    def __init__(self, outbound_endpoint):
        self.outbound_endpoint = outbound_endpoint
