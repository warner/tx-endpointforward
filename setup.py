from __future__ import absolute_import, print_function
from setuptools import setup

DESCRIPTION = """\
Listen on one endpoint, forward connections to a second endpoint. Like
'twistd portforward', but generalized to any kind of endpoint, not just TCP."""

setup(
    name="TxEndpointForward",
    description="forward one endpoint to another",
    long_description=DESCRIPTION,
    license="MIT",
    package_dir={"": "src"},
    packages=[
        "tx_endpointforward",
        #"twisted.plugins",
        ],
    install_requires=[
        "twisted",
        ],
    version="0.0.1",
    )
