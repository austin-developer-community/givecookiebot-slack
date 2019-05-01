# Contributing Guidelines

Thanks for helping out! There are plenty of typos to fix and features to add.
Getting started is easy!

## Installation

General installation is covered in the [README][readme]. Installing into
a [venv](https://docs.python.org/3/library/venv.html) is recommended.

[readme]: https://github.com/austin-developer-community/givecookiebot-slack/tree/master/README.rst

## Development

Install additional requirements from `requirements-dev.txt`:

```bash
pip install -r requirements-dev.txt
```

Ensure any additional contributions follow `pylint` guidelines.

## Building Documentation

Building documentation is not needed unless contributing to the documentation.

### HTML Docs

Install requirements specified in `requirements-docs.txt`. Move to `docs`
directory and build the HTML files:

```bash
$ make html
```

HTML files will be located in `../../givecookiebot-slack-docs/html/`.

### LaTeX PDF

Building the PDF has more requirements that vary based on the operating system.
For Ubuntu 18.04:

```bash
$ sudo apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-xetex
```

XeLaTeX, `texlive-xetex`, is needed for Unicode emojis to be inserted into the
PDF. Build the PDF from within the `docs` directory:

```bash
$ make latexpdf
```

The PDF is saved to `../givecookiebot-slack.pdf`. It may have to be built
multiple times to build without errors because the indexer sometimes fails.

## Code of Conduct

Whether submitting Issues or Pull Requests, be sure to follow the
[Code of Conduct][conduct].

[conduct]: https://github.com/austin-developer-community/givecookiebot-slack/tree/master/CODE_OF_CONDUCT.md

## Submit Bug/Issue/Enhancement

Open an issue in the [GitHub Issue tracker][tracker] following the
[Issue template][issuetemplate]. Be as detailed as you can to help identify the
bug.

[tracker]: https://github.com/austin-developer-community/givecookiebot-slack/issues
[issuetemplate]: https://github.com/austin-developer-community/givecookiebot-slack/tree/master/.github/ISSUE_TEMPLATE.md

## Submit Pull Request

Whether adding a feature or fixing a bug, open a pull request in
[GitHub][pulls] following the [Pull request template][prtemplate].

[pulls]: https://github.com/austin-developer-community/givecookiebot-slack/pulls
[prtemplate]: https://github.com/austin-developer-community/givecookiebot-slack/tree/master/.github/PULL_REQUEST_TEMPLATE.md

## Contact

Our [Facebook group][contact] has a link to the Slack workspace where
questions can be asked in the `#general` channel or concerns can be raised by
Direct Messaging the project team.

[contact]: https://www.facebook.com/groups/220313165320803/
