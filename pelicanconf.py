#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Thomas Delatte'
SITENAME = "Thomas Delatte's blog"
SITEURL = 'https://thomasdelatte.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)


DEFAULT_PAGINATION = 10

SITE_AUTHOR = 'Thomas Delatte'
TWITTER_USERNAME = '@thomasdelatte'
INDEX_DESCRIPTION = 'Website and blog of Thomas Delatte, data scientist and lawyer from Brussels.'

SIDEBAR_LINKS = [
    '<a href="/about/">About</a>',
    '<a href="/archive/">Portfolio</a>'
]

ICONS_PATH = 'images/icons'

SOCIAL_ICONS = [
    ('https://twitter.com/thomasdelatte', 'Twitter', 'fa-twitter'),
    ('https://github.com/ThomasDelatte', 'GitHub', 'fa-github'),
    ('https://linkedin/in/thomasdelatte', 'LinkedIn', 'fa-linkedin')
]

THEME_COLOR = '#FF8000'

# Pelican settings
RELATIVE_URLS = True
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 42

THEME = 'pneumatic'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archive/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Disable authors, categories, tags, and category pages
DIRECT_TEMPLATES = ['index', 'archives']
CATEGORY_SAVE_AS = ''

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {'linenums': None},
        'markdown.extensions.extra': {},
    },
    'output_format': 'html5',
}

CACHE_CONTENT = False
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'develop'
PATH = 'content'

templates = ['404.html']
TEMPLATE_PAGES = {page: page for page in templates}

STATIC_PATHS = ['images/icons', 'images/articles', 'extra']
IGNORE_FILES = ['.DS_Store', 'pneumatic.scss', 'pygments.css', '.ipynb_checkpoints']


EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/favicon.ico': {'path': 'favicon.ico'}}
extras = ['CNAME', 'favicon.ico', 'robots.txt']
IPYNB_USE_METACELL = True

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['plugins', '/home/tdelatte/projects/pelican/plugins']
PLUGINS = ['assets', 'neighbors', 'render_math', 'ipynb.markup']
ASSET_SOURCE_PATHS = ['static']
ASSET_CONFIG = [
    ('cache', False),
    ('manifest', False),
    ('url_expire', False),
    ('versions', False),
]

GOOGLE_ANALYTICS = 'UA-163901213-1'