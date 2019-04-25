"""givecookiebot-slack

Defines `Event API`_ events that the bot will respond to.

.. _Event API: https://api.slack.com/events-api
"""

import os

from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
from flask import Flask


app = Flask(__name__)  # pylint: disable=invalid-name
