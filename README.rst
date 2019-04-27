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
  export SLACK_BOT_SCOPE="third_long_complicated_string_here"

Next, run ``tokens.py`` to get the ``user`` and ``bot`` tokens that will be
used to access the Slack API.

License
-------

`GPLv3 License <LICENSE>`_ © Austin Developer Community
