Specify title, like:

> Feature: Add [BLANK] feature
> Bug: [BLANK] isn't working
> Discussion: I'm worried about [BLANK]

## Description

[provide general introduction to the issue logging and why it is relevant to this repository]

## Context

[provide more detailed introduction to the issue itself and why it is relevant]

## Process

[ordered list the process to finding and recreating the issue, example below]

1. User goes to delete a dataset (to save space or whatever)
2. User gets popup modal warning
3. User deletes and it's lost forever

## Expected result

[describe what you would expect to have resulted from this process]

## Current result

[describe what you you currently experience from this process, and thereby explain the bug]

## Possible Fix

[not obligatory, but suggest fixes or reasons for the bug]

* Modal tells the user what dataset is being deleted, like “You are about to delete this dataset: car_crashes_2014.”
* A temporary "Trashcan" where you can recover a just deleted dataset if you mess up (maybe it's only good for a few hours, and then it cleans the cache assuming you made the right decision).

## `name of issue` screenshot

[if relevant, include a screenshot]

## System and environment information

[provide what OS version, Python version, and modules are installed, example below]

OS version (for Ubuntu):

```bash
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.2 LTS
Release:        18.04
Codename:       bionic
```

Python version and modules:

```bash
$ python --version
Python 3.6.7

$ pip freeze > environment.txt && cat environment.txt
alabaster==0.7.12
astroid==2.2.5
Babel==2.6.0
certifi==2019.3.9
chardet==3.0.4
Click==7.0
docutils==0.14
Flask==1.0.2
idna==2.8
imagesize==1.1.0
...
```
