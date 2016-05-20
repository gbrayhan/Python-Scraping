import re
import urllib2
import urlparse

def link_crawler(seed_url, link_regex):
	crawl_queue = [seed_url]
	# keep track which URL's have seen before
	seen = set(crawl_queue)
	while crawl_queue: #siempre que exista crawl_queue
		url = crawl_queue.pop()#Quitar de la lista y regresar ultimo elemento
		html = urllib2.urlopen(url).read()
		for link in get_links(html): # en get links se encuentran todas las terminaciones /###
			# check if link matches expected regex
			if re.match(link_regex, link):
				# form absolute link
				link = urlparse.urljoin(seed_url, link)
				# check if have already seen this link
				if link not in seen:
					seen.add(link)
					crawl_queue.append(link)
			print url+link #Tomar Nota 
			#print urllib2.urlopen(url+link).read()


def get_links(html):
	"""Return a list of links from html
	"""
	# a regular expression to extract all links from the webpage
	webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
	# list of all links from the webpage
	return webpage_regex.findall(html)


link_crawler('http://example.webscraping.com','example.webscraping.com/(index|view)/')