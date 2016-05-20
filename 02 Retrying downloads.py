import urllib2
def download(url, num_retries=2): #Numero de peticiones
	print 'Downloading:', url
	try:
		html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print 'Download error:', e.reason
		html = None
	if num_retries > 0:
		if hasattr(e, 'code') and 200 <= e.code < 524:
			# recursively retry 5xx HTTP errors
			return download(url, num_retries-1)
		return html


print download("http://httpstat.us/400") #Importante el protocolo
