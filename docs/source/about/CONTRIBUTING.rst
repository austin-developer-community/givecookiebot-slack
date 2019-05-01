Contributing Guidelines
=======================

Thanks for helping out! There are plenty of typos to fix and features to add.
Getting started is easy!

Installation
------------

General installation is covered in the `README`_. Installing into
a `venv <https://docs.python.org/3/library/venv.html>`_ is recommended.

.. _README: https://github.com/austin-developer-community/givecookiebot-slack/tree/master/README.rst

Development
-----------

Install additional requirements from ``requirements-dev.txt``:

.. code-block:: bash

  pip install -r requirements-dev.txt


Ensure any additional contributions follow ``pylint`` guidelines.

Building Documentation
----------------------

Building documentation is not needed unless contributing to the documentation.

HTML Docs
^^^^^^^^^

Install requirements specified in ``requirements-docs.txt``. Move to ``docs``
directory and build the HTML files:

.. code-block:: bash

  $ make html

HTML files will be located in ``../../givecookiebot-slack-docs/html/``.

LaTeX PDF
^^^^^^^^^

Building the PDF has more requirements that vary based on the operating system.
For Ubuntu 18.04:

.. code-block:: bash

  $ sudo apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-xetex

XeLaTeX, ``texlive-xetex``, is needed for Unicode emojis to be inserted into the
PDF. Build the PDF from within the ``docs`` directory:

.. code-block:: bash

  $ make latexpdf

The PDF is saved to ``../givecookiebot-slack.pdf``. It may have to be built
multiple times to build without errors because the indexer sometimes fails.

Code of Conduct
---------------

Whether submitting Issues or Pull Requests, be sure to follow the
`Code of Conduct`_.

.. _Code of Conduct: https://github.com/austin-developer-community/givecookiebot-slack/tree/master/CODE_OF_CONDUCT.md

Submit Bug/Issue/Enhancement
----------------------------

Open an issue in the `GitHub Issue tracker`_ following the
`Issue template`_. Be as detailed as you can to help identify the
bug.

.. _GitHub Issue tracker: https://github.com/austin-developer-community/givecookiebot-slack/issues
.. _Issue template: https://github.com/austin-developer-community/givecookiebot-slack/tree/master/.github/ISSUE_TEMPLATE.md

Submit Pull Request
-------------------

Whether adding a feature or fixing a bug, open a pull request in
`GitHub`_ following the `Pull request template`_.

.. _GitHub: https://github.com/austin-developer-community/givecookiebot-slack/pulls
.. _Pull request template: https://github.com/austin-developer-community/givecookiebot-slack/tree/master/.github/PULL_REQUEST_TEMPLATE.md

Contact
-------

Our `Facebook group`_ has a link to the Slack workspace where
questions can be asked in the ``#general`` channel or concerns can be raised by
Direct Messaging the project team.

.. _Facebook group: https://www.facebook.com/groups/220313165320803/
