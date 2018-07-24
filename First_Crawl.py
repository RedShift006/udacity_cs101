# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-07-23 22:24:29
# @Last Modified by:   Administrator
# @Last Modified time: 2018-07-24 00:44:04


# https://udacity.github.io/cs101x/index.html

def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1: end_quote]
	return url, end_quote

def get_all_links(page, tocrawl):
	while True:
		url, endpos = get_next_target(page)
		if url:
			tocrawl.append(url)
			page= page[endpos: ]
		else:
			break
	# return tocrawl


import urllib2

def get_page_content(url):
	response = urllib2.urlopen(url)
	page = response.read()
	return page


# page = get_page_content('https://udacity.github.io/cs101x/index.html')

# get_all_links(page)

def crawl_web(seed_url):
	tocrawl = [seed_url]
	crawled = []
	while len(tocrawl) != 0:
		url = tocrawl.pop()
		if url not in crawled:
			crawled.append(url)
			page_content = get_page_content(url)
			get_all_links(page_content, tocrawl)
			
	return crawled


start_url = "https://udacity.github.io/cs101x/index.html"
for e in crawl_web(start_url):
        print e
