#!/usr/bin/env python

"""Module to test the basic interactions with an Arista vEOS Switch using eAPI.

Attributes:
    SWITCH_IP (str): The Default IP address for the Switch
    SWITCH_PWD (str): The Default Password for the Switch
    SWITCH_USER (str): The Default Username for the Switch
"""

from eapi import AristaSwitch

SWITCH_IP = '10.10.10.11'
SWITCH_USER = 'admin'
SWITCH_PWD = 'admin'


class FailError(Exception):
    """A custom exception class for Test Failures."""

    def __init__(self, arg):
        """Initialize the FailError object."""
        Exception.__init__(
            self, "An error occured while executing the testcase")


class TestBasics(object):
    """
    This class defines the tests which cover the basic funtionalities of an
    user interacting with the Arista vEOS Switch eAPI using AristaSwitch class.
    """

    def test_basic_api_connection(self):
        """Scenario: The user should be able to connect to the API.

        Connect to the Device
        Get Version Info
        """
        try:
            device = AristaSwitch(SWITCH_USER, SWITCH_PWD, SWITCH_IP)
            version_info = device.get_version_info()[0]

            expected_version = '4.20.1F'
            parsed_version = version_info['version']

            msg = "Parsed Version is not matching the Expected Version"
            assert(parsed_version == expected_version), msg
        except Exception as e:
            print e.message
            raise FailError(
                "An error occured while executing test: test_basic_api_connection")
