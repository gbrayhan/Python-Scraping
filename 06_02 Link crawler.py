import re
import urllib2
import urlparse


def link_crawler(seed_url, link_regex):
	"""Crawl from the given seed URL following links matched by link_regex
	"""
	crawl_queue = [seed_url]
	while crawl_queue:
		url = crawl_queue.pop()
		html = urllib2.urlopen(url).read()
		for link in get_links(html):
			if re.match(link_regex, link):
				link = urlparse.urljoin(seed_url, link)
				crawl_queue.append(link)
			print url+link #Tomar Nota 
			print urllib2.urlopen(url+link).read()

def get_links(html):
	"""Return a list of links from html
	"""
	# a regular expression to extract all links from the webpage
	webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
	# list of all links from the webpage
	return webpage_regex.findall(html)


link_crawler('http://example.webscraping.com','example.webscraping.com/(index|view)/')