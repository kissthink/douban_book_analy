#
# douban_techbook_analy.py
# -*- coding: utf-8 -*-

import urllib
import urllib2
from bs4 import BeautifulSoup

baseUrl = "http://www.douban.com/tag/%E7%BC%96%E7%A8%8B/book"
baseIndex = 0

vdisk_search_prefix_url = "http://vdisk.weibo.com/search/?type=public&"

def analy_page_books(html_data):
	soup = BeautifulSoup(html_data)
	print html_data
	for book in soup.find_all("a", class_="title"):
		print book.get_text()
		collect_vdisk(book.get_text())
		break

def collect_vdisk(name):

	#search_vdisk_url = vdisk_search_prefix_url + urllib.urlencode(name.encode('utf-8'))

	params = {}
	params['keyword'] = name.encode("UTF-8")

	search_vdisk_url = vdisk_search_prefix_url + urllib.urlencode(params)

	print "search_vdisk_url => %s" % search_vdisk_url
	searchReq = urllib2.urlopen(search_vdisk_url)
	searchBookData = searchReq.read()

	print searchBookData

	pass

while True:
	booksUrl = baseUrl
	if baseIndex >= 1:
		booksUrl = baseUrl + "?start=%d" % (15 * baseIndex)

	booksReq = urllib2.urlopen(booksUrl)
	booksData = booksReq.read()
	analy_page_books(booksData)

	baseIndex = baseIndex + 1
	if baseIndex >= 2:
		break