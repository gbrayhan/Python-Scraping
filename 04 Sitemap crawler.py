import urllib2
import re

def crawl_sitemap(url):
	# download the sitemap file
	sitemap =urllib2.urlopen(url).read()
	#print sitemap
	# extract the sitemap links
	links = re.findall(r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', sitemap)[:4]
	print links

	# download each link
	for link in links:
		for l in link:
			
			# scrape html here
			if l==link[0]:
				try:
					html = urllib2.urlopen(l).read()

				except urllib2.URLError as e:

					print 'Download error:', e.reason
					html = None
				print html
	

crawl_sitemap('http://relopezbriega.github.io/blog/2015/07/19/expresiones-regulares-con-python/')