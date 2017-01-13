#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'lyxw'
SITENAME = u'lyxw blog'
SITEURL = 'https://lyxw.github.io'
DISQUS_SITENAME = 'lyxw'
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh_CN'

DEFAULT_DATE_FORMAT = ('%Y-%m-%d(%A) %H:%M')
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'hide'

THEME = "themes/blueidea"


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


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




# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/lyxw'),
          ('lastfm', 'http://lastfm.com/user/lyxw'),
          ('github', 'https://github.com/lyxw'),)

#DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
