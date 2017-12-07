'''
module docstring
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Graham Chester'
SITENAME = 'GCHESTER.COM'
SITEURL = 'http://localhost:8000'
THEME = 'themes/pelican-bootstrap3'  # 'themes/tuxlite_tbs'

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
SOCIAL = (('Facebook', 'http://facebook.com/graham.chester'),
          ('Twitter', 'http://twitter.com/gchester99'),
          ('LinkedIn', 'http://www.linkedin.com/in/graham-chester-051b176'),
          ('StackOverflow', 'http://stackoverflow.com/users/3972759/graham-c?tab=profile'),
         )

DEFAULT_PAGINATION = 5
#RELATIVE_URLS = False

# GC custom settings
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'guess_lang': False,
            },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        },
    'output_format': 'html5',
}


#MD_EXTENSIONS = ['codehilite(guess_lang=False, css_class=highlight)', 'extra']
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
DEFAULT_DATE = 'fs'
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git', '.gitignore']
TWITTER_USERNAME = 'gchester99'
#MENUITEMS = [('GitHub','https://github.com/chesters99'),]

STATIC_PATHS = ['static', 'images', 'pdfs']
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
    'static/custom.css': {'path': 'custom.css'},
    'static/CNAME': {'path': 'CNAME'},
}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['tag_cloud', 'ipynb.markup', 'tipue_search', 'sitemap']
MARKUP = ('md', 'rst', 'ipynb')
IPYNB_USE_META_SUMMARY = True
TAG_CLOUD_STEPS = 1
TAG_CLOUD_MAX_ITEMS = 10

ARCHIVES_SAVE_AS = 'archives.html'
SITELOGO = 'images/gchester.png'
#AVATAR = 'images/gchester.png'
ABOUT_ME = 'Data Science Guy, Python Developer, and ex-Financial Systems Consultant'
BANNER = 'images/space.jpg'
BANNER_SUBTITLE = 'Data Science and Python'
BANNER_ALL_PAGES = True

GITHUB_SHOW_USER_LINK = False
GITHUB_USER = 'chesters99'
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
#DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
USE_OPEN_GRAPH = True
#OPEN_GRAPH_IMAGE = 'images/gchester.png'
CUSTOM_CSS = 'custom.css'
PYGMENTS_STYLE = 'emacs'
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

