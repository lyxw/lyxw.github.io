#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://lyxw.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True


# menu items
MENUITEMS = [('Archives', 'archives'),
	    ('About', 'about.html'),]
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

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
