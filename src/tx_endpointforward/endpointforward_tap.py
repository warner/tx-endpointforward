from . import forwarder
from twisted.internet import reactor
from twisted.python import usage
from twisted.application.internet import StreamServerEndpointService
from twisted.internet import endpoints

LONGDESC = """\
This plugin sets up a 'inbound' listening endpoint. Any connections that are
received on the inbound endpoint are forwarded to the 'outbound' endpoint.
Each time an inbound connection is established, a new outbound connection is
initiated, and if/when it completes, the two connections are glued together.

If the outbound connection fails to connect, the inbound connection is
dropped (which is unfortunately indistinguishable from a connection that
succeeded but then closed without sending any data).

The 'inbound'/'outbound' arguments can be arbitrary server/client endpoint
descriptors. For a basic TCP forwarder, the inbound endpoint should be
something like 'tcp:12345:interface=localhost', and the outbound endpoint
should be like 'tcp:example.org:7890'.
"""

class Options(usage.Options):
    #synopsis = "INBOUND OUTBOUND"
    longdesc = LONGDESC

    optParameters = [
        ("inbound", "i", None, "inbound (listening) endpoint specification"),
        ("outbound", "o", None, "outbound endpoint specification"),
        ]

    def postOptions(self):
        if not self["inbound"] or not self["outbound"]:
            raise usage.UsageError("--inbound= and --outbound are required")

def makeService(config, reactor=reactor):
    outbound_ep = endpoints.clientFromString(reactor, config["outbound"])
    f = forwarder.EndpointProxyFactory(outbound_ep)
    inbound_ep = endpoints.serverFromString(reactor, config["inbound"])
    return StreamServerEndpointService(inbound_ep, f)

