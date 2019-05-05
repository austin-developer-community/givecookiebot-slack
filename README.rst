givecookiebot-slack
===================

**givecookiebot-slack** is a Slack bot that adds a cookie emoji (``🍪``) to a
user's status for 3 hours when that user is 'given' a cookie in chat.

Something like::

  @User Thanks for helping out today! 🍪

The user's status will then be updated to include the cookie emoji.

After 3 hours have passed, the cookie emoji is removed from the user's status.

Installation
------------

**givecookiebot-slack** is a Python script that requires a few dependencies
specified in ``requirements.txt``.

.. code-block:: bash

  pip install -r requirements.txt

With the Python requirements installed, we can move on to Slack API's
requirements.

Slack API Tokens
^^^^^^^^^^^^^^^^

First, the Slack client tokens must be added to the environment variables in
``~/.bashrc``:

.. code-block:: bash

  export SLACK_CLIENT_ID="first_long_complicated_string_here"
  export SLACK_CLIENT_SECRET="second_long_complicated_string_here"
  export SLACK_SIGNING_SECRET="third_long_complicated_string_here"
  export SLACK_BOT_SCOPE="channels:history users.profile:write"

Next, run ``tokens.py`` to get the ``user`` and ``bot`` tokens that will be
used to access the Slack API.

.. code-block:: bash

  $ cd givecookiebot-slack  # Go to source code directory (if needed)
  $ source ./venv/bin/activate  # Activate venv (if applicable)
  (venv)$ python -m givecookiebotslack.tokens

The Flask server is running at ``127.0.0.1:5000``, by default. Go to
http://127.0.0.1:5000/begin_auth and click on ``Add to Slack`` to start the
OAuth process.

Once **givecookiebot-slack** gets approval for the needed scopes and
permissions, the user and bot tokens should be saved to the
``SLACK_USER_TOKEN`` and ``SLACK_BOT_TOKEN`` environment variables,
respectively.

ngrok
^^^^^

One can use `ngrok`_ as a quick way to access the local Flask server externally.

.. note::

    Using ``ngrok`` requires making an account. Free accounts have dynamic domain
    names that change every 8 hours or when the terminal is closed.

Once the local Flask server is running, start ``ngrok`` with:

.. code-block:: bash

  ngrok http 5000

Use either the ``http`` or ``https`` forwarding address:
``xxxxxxxx.ngrok.io/begin_auth``.

.. _ngrok: https://ngrok.com/

Start givecookiebot-slack
^^^^^^^^^^^^^^^^^^^^^^^^^

With the tokens saved, start **givecookiebot-slack** in a new terminal with:

.. code-block:: bash

  $ cd givecookiebot-slack  # Go to source code directory (if needed)
  $ source ./venv/bin/activate  # Activate venv (if applicable)
  (venv)$ python -m givecookiebotslack.bot

The Flask server is running at ``127.0.0.1:3000``, by default. The bot will be
waiting for events from slack at the address http://127.0.0.1:3000/slack/events.

Navigating there should render a page that says "These are not the slackbots
you're looking for."

Once again, use ``ngrok`` to register the bot with Slack Events at
https://api.slack.com/apps with:

.. code-block:: bash

  ngrok http 3000

Provide the ``https`` forwarding link as the Request URL:
``https://xxxxxxxx.ngrok.io/slack/events``.

Add the bot to a channel and start passing out 🍪.

License
-------

`GPLv3 License <LICENSE>`_ © Austin Developer Community
