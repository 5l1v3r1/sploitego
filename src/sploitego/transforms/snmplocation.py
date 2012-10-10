#!/usr/bin/env python

from sploitego.scapytools.snmp import SNMPManager, SNMPError
from canari.maltego.message import UIMessage
from canari.maltego.entities import Location
from common.entities import SNMPCommunity
from canari.framework import configure
from common.snmp import snmpargs


__author__ = 'Nadeem Douba'
__copyright__ = 'Copyright 2012, Sploitego Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Nadeem Douba'
__email__ = 'ndouba@gmail.com'
__status__ = 'Development'

__all__ = [
    'dotransform'
]


@configure(
    label='To Location [SNMP]',
    description='This transform uses SNMP to retrieve the location of the device being queried.',
    uuids=['sploitego.v2.SNMPCommunityToLocation_SNMP'],
    inputs=[('Reconnaissance', SNMPCommunity)]
)
def dotransform(request, response):
    try:
        s = SNMPManager(*snmpargs(request))
        response += Location(s.location)
    except SNMPError, s:
        response += UIMessage(str(s))
    return response


