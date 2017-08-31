#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ian Laird'
SITENAME = u'IanRLaird.com'
# SITESUBTITLE = ""
# SITEURL = 'ianrlaird.com'

GITHUB_USERNAME = "en0"
BLOG_START_YEAR = "2016"

PATH = 'content'

TIMEZONE = 'America/Boise'

DEFAULT_LANG = u'en'

THEME = './theme/lazystrap'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/en0'),
        ('Linkedin', 'https://www.linkedin.com/in/ian-laird-64916131'),)

DEFAULT_PAGINATION = 10

TAG_URL = 'tag/{slug}/index.html'
TAG_SAVE_AS = 'tag/{slug}'
AUTHOR_URL = 'author/{slug}/index.html'
AUTHOR_SAVE_AS = 'author/{slug}'
ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'
PAGINATED_DIRECT_TEMPLATES = ('archives',)
PAGINATION_PATTERNS = (
    (1, '{name}/', '{name}/index.html'),
    (2, '{name}/page{number}/', '{name}/page{number}/index.html')
)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
