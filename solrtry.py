import solr
s = solr.Solr('http://localhost:8983/solr/gettingstarted')
response = s.select("arsenal")
#print response.results
for hit in response.results:
	 print hit['text']
