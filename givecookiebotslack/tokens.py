"""Get User and Bot tokens.

Uses Slack's `OAuth 2.0`_ to fetch the User and Bot tokens for interfacing with
Slack's API.

.. _OAuth 2.0: https://slack.dev/python-slackclient/auth.html#the-oauth-flow
"""

import os

from flask import Flask, request
from slackclient import SlackClient

CLIENT_ID = os.environ["SLACK_CLIENT_ID"]
CLIENT_SECRET = os.environ["SLACK_CLIENT_SECRET"]
OAUTH_SCOPE = os.environ["SLACK_BOT_SCOPE"]

app = Flask(__name__)  # pylint: disable=invalid-name

@app.route("/begin_auth", methods=["GET"])
def pre_install():
    """Directs user to Slack's OAuth acceptance page.
    """
    return '''
        <a href="https://slack.com/oauth/authorize?scope={0}&client_id={1}">
            Add to Slack
        </a>
    '''.format(OAUTH_SCOPE, CLIENT_ID)

@app.route("/finish_auth", methods=["GET", "POST"])
def post_install():
    """Gets tokens from auth completion page.
    """

    # Retrieve the auth code from the request params
    auth_code = request.args['code']

    # An empty string is a valid token for this request
    slack_client = SlackClient("")

    # Request the auth tokens from Slack
    auth_response = slack_client.api_call(
        "oauth.access",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        code=auth_code
        )

    # Save the bot token to an environmental variable or to your data store
    # for later use
    # TODO: Add SLACK_SIGNING_SECRET to environment variables? OAuth1 vs 2
    os.environ["SLACK_USER_TOKEN"] = auth_response['access_token']
    os.environ["SLACK_BOT_TOKEN"] = auth_response['bot']['bot_access_token']

    # Don't forget to let the user know that auth has succeeded!
    return "Auth complete!"

if __name__ == '__main__':
    app.run(debug=True)
