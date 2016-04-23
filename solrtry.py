import solr
import re
s = solr.Solr('http://localhost:8983/solr/gettingstarted')
def media( term ):
	response = s.select(term + "http* " , rows = 50)
	return response

def media( term, lang):
	#searchterm = term + "http*" + 
	response = s.select(term +" " "http*  lang:" + " " + lang, rows = 50)
	return response
		
tweets = []
links = []

#y = "fr"
#response = s.select(" arsenal http*  lang:" + y, rows = 50)
#print response.results
#response2 = s.select("")
#print response
response = media( "arsenal", "fr")
for hit in response.results:
	 tweets.append(  hit['text'] )
	 links.append( re.search( "(?P<url>https?://[^\s]+)","".join(hit['text']) ).group("url"))

print links
#print tweets

