import urllib2
import itertools

def crawl_sitemap(url):

	for page in itertools.count(1,2): #[start,step]
		pg = url + '/-%d' % page
		html = urllib2.urlopen(pg).read()
		if html is None:
			break
		else:
			print pg
			print html
		pass


crawl_sitemap("http://example.webscraping.com/view")

