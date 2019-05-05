"""givecookiebot-slack

Defines `Event API`_ events that the bot will respond to.

Attributes:
    SLACK_SIGNING_SECRET (str): Secret identifying bot to Slack Events API. Like a password.
    SLACK_USER_TOKEN (str): Token used to access Slack Web API.
    slack_events_adapter (SlackEventAdapter): Instance of :py:class:`SlackEventAdapter`.
    slack_client (SlackClient): Instance of :py:class:`SlackClient`.
    USERMENTION_RE (re.compile): Regular expression object matching a user mention pattern.

.. _Event API: https://api.slack.com/events-api
"""

import os
import re
from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient

# Our app's Slack Event Adapter for receiving actions via the Events API
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack/events")  #pylint: disable=invalid-name

# Create a SlackClient for your bot to use for Web API requests
# Admin user token is needed to modify user profiles
SLACK_USER_TOKEN = os.environ["SLACK_USER_TOKEN"]
slack_client = SlackClient(SLACK_USER_TOKEN)  # pylint: disable=invalid-name

# Regular expressions
USERMENTION_RE = re.compile(r'''
                            <                    # open bracket (required)
                            @                    # @ symbol (required)
                            (?P<user_id>\w{9})   # 9 alphanumeric characters (required)
                            >                    # close bracket (required)
                            ''', re.VERBOSE)

@slack_events_adapter.on("message")
def handle_message(event_data: dict):
    """Message handler

    Parses message for cookie emoji (🍪) and a user mention, then changes
    mentioned user's status to include cookie emoji for 3 hours.

    Returns:
        True if successful, otherwise the error code given by the Slack API.
    """
    message = event_data["event"]
    text = message.get('text')
    match = USERMENTION_RE.search(text)
    # If the incoming message contains "🍪" and a user mention.
    if all([":cookie:" in text, match]):
        user_id = match.group('user_id')
        expiration = float(message.get('ts')) + (3600 * 3)  # 3 hours from now
        # Change mentioned user's status to include cookie emoji and expiration time.
        response = slack_client.api_call("users.profile.set", user=user_id,
                                         status_text='earned',
                                         status_emoji=':cookie:',
                                         status_expiration=str(expiration))
        # Confirm response to status change is ok.
        if not response['ok']:
            return response['error']
    return True

@slack_events_adapter.on("error")
def error_handler(err):
    """Error events
    """
    print("ERROR: " + str(err))

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
if __name__ == '__main__':
    slack_events_adapter.start(port=3000)
