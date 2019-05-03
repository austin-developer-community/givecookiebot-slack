"""givecookiebot-slack

Defines `Event API`_ events that the bot will respond to.

Attributes:
    SLACK_SIGNING_SECRET (str): Secret identifying bot to Slack Events API. Like a password.
    SLACK_BOT_TOKEN (str): Token used to access Slack Web API.
    slack_events_adapter (SlackEventAdapter): Instance of :py:class:`SlackEventAdapter`.
    slack_client (SlackClient): Instance of :py:class:`SlackClient`.

.. _Event API: https://api.slack.com/events-api
"""

import os
import re
from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient

# Our app's Slack Event Adapter for receiving actions via the Events API
SLACK_CLIENT_SECRET = os.environ["SLACK_CLIENT_SECRET"]
slack_events_adapter = SlackEventAdapter(SLACK_CLIENT_SECRET, "/slack/events")  #pylint: disable=invalid-name

# Create a SlackClient for your bot to use for Web API requests
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
slack_client = SlackClient(SLACK_BOT_TOKEN)  # pylint: disable=invalid-name

@slack_events_adapter.on("message")
def handle_message(event_data):
    """Example responder to greetings
# Regular expressions
usermention_re = re.compile(r'''
                            <       # open bracket (required)
                            @       # @ symbol (required)
                            \w{9}   # 9 alphanumeric characters (required)
                            >       # close bracket (required)
''', re.VERBOSE)  # pylint: disable=invalid-name
    """
    message = event_data["event"]
    # If the incoming message contains "hi", then respond with a "Hello" message
    if message.get("subtype") is None and "hi" in message.get('text'):
        channel = message["channel"]
        message = "Hello <@%s>! :tada:" % message["user"]
        slack_client.api_call("chat.postMessage", channel=channel, text=message)

@slack_events_adapter.on("error")
def error_handler(err):
    """Error events
    """
    print("ERROR: " + str(err))

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
if __name__ == '__main__':
    slack_events_adapter.start(port=3000)
