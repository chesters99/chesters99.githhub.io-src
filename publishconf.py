'''
docstring
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

from __future__ import unicode_literals
import os
import sys

from pelicanconf import *

sys.path.append(os.curdir)
SITEURL = 'http://blog.gchester.com'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

GOOGLE_ANALYTICS = 'UA-55102590-1'
