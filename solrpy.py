import solr
tweetlist = []
s = solr.Solr('http://localhost:8983/solr/gettingstarted')
response = s.select('arsenal lang:fr',rows = 1000)
#print response
for x in response.results:
	print x
	"""
	tweetlist.append( str(x['text']) )
for item in tweetlist:
	print item
"""
"""
for hit in response.results:
	 print hit
"""