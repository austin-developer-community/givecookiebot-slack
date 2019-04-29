"""givecookiebot-slack

Defines `Event API`_ events that the bot will respond to.

.. _Event API: https://api.slack.com/events-api
"""

import os
from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient

# Our app's Slack Event Adapter for receiving actions via the Events API
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack/events")  #pylint: disable=invalid-name

# Create a SlackClient for your bot to use for Web API requests
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
slack_client = SlackClient(SLACK_BOT_TOKEN)  # pylint: disable=invalid-name

@slack_events_adapter.on("message")
def handle_message(event_data):
    """Example responder to greetings
    """
    message = event_data["event"]
    # If the incoming message contains "hi", then respond with a "Hello" message
    if message.get("subtype") is None and "hi" in message.get('text'):
        channel = message["channel"]
        message = "Hello <@%s>! :tada:" % message["user"]
        slack_client.api_call("chat.postMessage", channel=channel, text=message)


@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    """Example reaction emoji echo
    """
    event = event_data["event"]
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    slack_client.api_call("chat.postMessage", channel=channel, text=text)

@slack_events_adapter.on("error")
def error_handler(err):
    """Error events
    """
    print("ERROR: " + str(err))

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
if __name__ == '__main__':
    slack_events_adapter.start(port=3000)
