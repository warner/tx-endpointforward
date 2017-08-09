from twisted.application.service import ServiceMaker

TxEndpointForward = ServiceMaker(
    "Endpoint Forwarding",
    "tx_endpointforward.endpointforward_tap",
    "Forward one endpoint to another.",
    "endpointforward")
