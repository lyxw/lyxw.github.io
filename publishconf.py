#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

AUTHOR = u'lyxw'
SITENAME = u'lyxw blog'
SITEURL = 'https://lyxw.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh_CN'

DEFAULT_DATE_FORMAT = ('%Y-%m-%d(%A) %H:%M')
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'hide'

THEME = "themes/gum"


# menu items
MENUITEMS = [('Home', SITEURL),
            ('Archives', 'archives.html'),
            ('Category', 'categories.html'),
            ('Tag', 'tags.html'),
	        ('About', 'authors.html'),]
DEFAULT_PAGINATION = 10
MD_EXTENSIONS = [
	"extra",
	"toc",
	"headerid",
	"meta",
	"sane_lists",
	"smarty",
	"wikilinks",
	"admonition",
	"codehilite(guess_lang=False,pygments_style=emacs,noclasses=True)"]
CNZZ_ANALYTICS = True
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'


THEME = "themes/gum"


# Following items are often useful when publishing

#DISQUS_SITENAME = ""		DISQUS_SITENAME = 'lyxw'
#GOOGLE_ANALYTICS = ""

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/lyxw'),
          ('weibo', 'http://weibo.com/user/lyxw'),
          ('github', 'https://github.com/lyxw'),)

