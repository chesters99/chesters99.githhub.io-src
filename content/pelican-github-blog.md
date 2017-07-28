Title: Setting up a GitHub Pages blog with Pelican
Date: 2016-10-19
Category: Getting Started
Tags: Python, Pelican
Slug: pelican-github-blog
Authors: Graham Chester
Summary: How to setup a blog on GitHub with Pelican

I wanted to setup a blog website in the simplest way, and leveraging existing/known tools as mush as possible. I like Python (a lot) so after reading some reviews chose Pelican as the website generator. Pelican supports markdown and iPython notebooks amonsgt many other things - which seemed ideal. The folks at GitHub have kindly provided *GitHub Pages* which serves your website from a GitHub repo - nice. [All described here](https://pages.github.com/).

The code/config for my website is available [here](https://github.com/chesters99/ghpages)

## Basic Blog Setup

Setting up a basic blog using GitHub is a relatively simple task, as much of the setup defaults for you. In the next section I'll cover how to finesse your blog with a custom domain and get it setup on google analytics (amongst other things)

### Installation

**Login to GitHub with your userid (or create one), and create two new repositories** as explained [here](https://pages.github.com/)

+ Create a repo for the website (output HTML, CSS) called *yourusername.github.io*

+ Create a repo for your content called *ghpages* (or name of your choice)

**Clone the repo to your machine - to a *ghpages* directory**

```text
git clone https://github.com/yourusername.github.io-src ghpages
```

** Add a submodule for the pelican output ie the actual website HTML/CSS **

```text
git submodule add https://github.com/yourusername.github.io.git output
```

** Install pelican **

```text
pip install pelican
```

**Create a basic config/template with answers as follows:**

```text
$ pelican-quickstart

Welcome to pelican-quickstart v3.6.3.
This script will help you create a new Pelican-based website.
Please answer the following questions so this script can generate the files needed by Pelican.

Where do you want to create your new web site? [.]
What will be the title of this web site? Your Blog's name
Who will be the author of this web site? Your Name
What will be the default language of this web site? [en]
Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) Y
What is your URL prefix? (see above example; no trailing slash) http://yourusername.github.io
Do you want to enable article pagination? (Y/n) Y
How many articles per page do you want? [10] 5
What is your time zone? [Europe/Paris] Europe/London
Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) Y
Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) Y
Do you want to upload your website using FTP? (y/N) n
Do you want to upload your website using SSH? (y/N) n
Do you want to upload your website using Dropbox? (y/N) n
Do you want to upload your website using S3? (y/N) n
Do you want to upload your website using Rackspace Cloud Files? (y/N) n
Do you want to upload your website using GitHub Pages? (y/N) Y
Is this your personal page (username.github.io)? (y/N) Y
Done. Your new project is available at xxxxxxxxxxxxx\ghpages
```

This will create content and output directories, the pelicanconf.py and publishconf.py files and some supporting files. Essentially you put your content in content, then run *make* as described below and pelican writes the html/css in the output directory.

It is helpful to create three subdirectories in the content directory

```text
cd content
mkdir pages static images
```

Your non-blog pages (eg about) go in the pages directory, images in images(doh!), and any content you just want pelican to copy across directory goes in static.

### Install Themes and plugins

This is an optional step depending on your requirements. If you want more choice with css themes or additional functionality for generating sitemaps, or search bar, or reading iPython notebooks (and many others) then:

```text
cd ghpages
git clone https://github.com/getpelican/pelican-themes.git themes
git clone https://github.com/getpelican/pelican-plugins.git plugins
```

The example pelicanconf.py below shows how these can be used.

### Configuration

While the essential config requires little update, there are many options to control your site behaviour. The config for the dev/test server is in *pelicanconf.py* and this is overridden by the 'production' config in *publishconf.py*. Please see my pelicanconf.py file as a working example. The config is described in some detail in the pelican documentation

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Graham Chester'
SITENAME = 'GCHESTER.COM'
SITEURL = 'http://localhost:8000'
THEME = 'themes/pelican-bootstrap3'

PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('KD Nuggets', 'http://kdnuggets.com/'),
         ('Kaggle', 'http://kaggle.com/'),
         ('Open Data Science', 'http://opendatascience.com/'),
         )

# Social widget
SOCIAL = (('Facebook', 'http://facebook.com/xxxxxxxxxxxxxx'),
          ('Twitter', 'http://twitter.com/xxxxxxxxxx'),
          ('LinkedIn', 'http://www.linkedin.com/in/xxxxxxxxxxxxxxxxxxxxxx'),
          ('StackOverflow', 'http://stackoverflow.com/users/xxxxxxx/xxxxxxxx?tab=profile'),
          )

DEFAULT_PAGINATION = 5
#RELATIVE_URLS = False

# GC custom settings
MD_EXTENSIONS = ['codehilite(guess_lang=False, css_class=highlight)', 'extra']
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
DEFAULT_DATE = 'fs'
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git','.gitignore']  # delete output directory at each build but preserve git files
TWITTER_USERNAME = 'xxxxxxxxxx'

STATIC_PATHS = ['static', 'images', 'pdfs']
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
    'static/custom.css': {'path': 'custom.css'},
    'static/CNAME': {'path': 'CNAME'},
}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['tag_cloud', 'ipynb.markup','tipue_search','sitemap']
MARKUP = ('md', 'rst', 'ipynb')
TAG_CLOUD_STEPS = 1
TAG_CLOUD_MAX_ITEMS = 10

ARCHIVES_SAVE_AS = 'archives.html'
SITELOGO = 'images/xxxxxxxx.png'
ABOUT_ME = 'Financial Systems Consultant, Python Developer and aspiring Data Scientist'
BANNER = 'images/space.jpg'
BANNER_SUBTITLE = 'Data Science and Python'
BANNER_ALL_PAGES = True

GITHUB_SHOW_USER_LINK = False
GITHUB_USER = 'xxxxxxxxxx'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True

BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_NAVBAR_INVERSE = False
BOOTSTRAP_FLUID = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True

SHOW_ARTICLE_AUTHOR = True
SHOW_DATE_MODIFIED = True
SHOW_ARTICLE_CATEGORY = True

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
USE_OPEN_GRAPH = True
CUSTOM_CSS = 'custom.css'
PYGMENTS_STYLE ='emacs'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DEFAULT_CATEGORY = "General"
DISQUS_SITENAME = 'gchester'

# Configuration for the "sitemap" plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'always',
        'indexes': 'hourly',
        'pages': 'monthly'
    }
}
```

The production config is much simpler in publishconf.py. Only the site url, google analytics needed to be set.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://blog.xxxxxxxx.com'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

GOOGLE_ANALYTICS = 'UA-xxxxxxxx-x'
```

### Local Testing

Simple....

```text
make html $$ make serve
```

In your browser go to <http://localhost:8000>

### Deployment to GitHub Pages

As described above, your ghpages directory needs to be pushed to two GitHub repos. One for your config, articles, pages, themes, plugins etc. And another for the pelican-generated website files.

Firstly make sure you have a .gitignore file in your ghpages directoryi, something like:

```text
$ cat .gitignore
output/
plugins/
themes/
__pycache__/
```

To push all your content/config changes to GitHub:

```text
cd ghpages
git add .
git commit -m "decriptive commit message"
git push -u origin master
```

Then to generate and push your website HTML/CSS etc to GitHub to be served

```text
make publish
cd output
git add .
git commit -m "update website"
git push -u origin master
```

### Checkout your new blog

In your browser goto <http://yourusername.github.io> and revel in the glory of your new blog!

In the second article I'll cover some ways to make your blog a little more professsional
