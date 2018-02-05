#!/usr/bin/env python

"""Module to interact with an Arista vEOS Switch using eAPI.

Attributes:
    SWITCH_IP (str): The Default IP address for the Switch
    SWITCH_PWD (str): The Default Password for the Switch
    SWITCH_USER (str): The Default Username for the Switch
"""

import ssl
from jsonrpclib import Server
from pprint import pprint

SWITCH_IP = '10.10.10.11'
SWITCH_USER = 'admin'
SWITCH_PWD = 'admin'

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


class ConfigError(Exception):
    """A custom exception class for Config Errors."""

    def __init__(self):
        """Initialize the ConfigError object."""
        Exception.__init__(self, "Error in configuring the switch")


class AristaSwitch(object):
    """Setup a connection to an Arista Switch.

    Attributes:
        api_auth_endpoint (str): The API Endpoint for the Arista Switch with
                                 the authorization information
        connection (object): An object of ServerProxy class providing a
                             connection to the Switch through the API
    """

    def __init__(self, username, password, ipaddress):
        """Initialize an object of Arista Switch by connecting to the API endpoint.

        Args:
            username (str): The Username for the Switch
            password (str): The Password for the Switch
            ipaddress (str): The IP address for the Switch
        """
        self.api_auth_endpoint = 'https://{}:{}@{}/command-api'.format(
            username, password, ipaddress)
        self.connection = Server(self.api_auth_endpoint)

    def get_version_info(self):
        """Get the version information of the Arista Switch.

        Returns:
            response (JSON object): A response containing the version
                                    information of the Switch

        Raises:
            ConfigError: A ConfigError is raised if an exception occurs while
                         running the commands
            TODO:
            1. Catch more specific exceptions, instead of a catch-all.
        """
        try:
            response = self.connection.runCmds(1, ["show version"])
            return response
        except Exception as e:
            print e.message
            raise ConfigError("ERROR: Could not get the version information")

    def add_vlans(self, vlans):
        """Configure vlan(s) on the Arista Switch.

        Args:
            vlans (list): A list of vlan IDs to be configured on the Switch

        Raises:
            ConfigError: A ConfigError is raised if an exception occurs while
                         running the commands
            TODO:
            1. Catch more specific exceptions, instead of a catch-all.
            2. Raise an exception for empty list of vlans
            3. Raise/Handle unknown data types passed to vlans
        """
        try:
            for vlan in vlans:
                vlan_config = "vlan {}".format(vlan)
                response = self.connection.runCmds(
                    1, ["enable", "configure", vlan_config])

                if type(response) is dict:
                    if 'error' in response.keys():
                        msg = "Error in configuring vlan {} \n".format(vlan)
                        msg += "Error: {}".format(response['message'])
                        raise ConfigError(msg)
        except Exception as e:
            print e.message
            raise ConfigError("ERROR: Could not configure vlans")

    def show_vlans(self, vlans):
        """Show the vlan(s) configuration on the Arista Switch.

        Args:
            vlans (list): A list of vlan IDs to be configured on the Switch

        Returns:
            vlan_info (list): A list of vlan(s) information from the Switch

        Raises:
            ConfigError: A ConfigError is raised if an exception occurs while
                         running the commands
            TODO:
            1. Catch more specific exceptions, instead of a catch-all.
            2. Raise an exception for empty list of vlans
            3. Raise/Handle unknown data types passed to vlans
        """
        vlan_info = []
        try:
            for vlan in vlans:
                vlan_config = "show vlan {}".format(vlan)
                response = self.connection.runCmds(1, [vlan_config])

                if type(response) is dict:
                    if 'error' in response.keys():
                        msg = "Error in getting vlan {} \n".format(vlan)
                        msg += "Error: {}".format(response['message'])
                        raise ConfigError(msg)

                vlan_info.append(response)

            return vlan_info
        except Exception as e:
            print e.message
            raise ConfigError("ERROR: Could not configure vlans")


if __name__ == "__main__":
    device = AristaSwitch(SWITCH_USER, SWITCH_PWD, SWITCH_IP)
    version_info = device.get_version_info()
    device.add_vlans([1, 2, 3, 4])
    pprint(device.show_vlans([1, 2, 3, 4]))
