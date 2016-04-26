#!/usr/bin/python
import cgi
import cgitb
import sys
import re
import operator
import math
reload(sys)
cgitb.enable()
from urllib2 import urlopen
import json as simplejson

import pprint
sys.setdefaultencoding('utf-8')
form = cgi.FieldStorage()
displayQuery = ""
if "searchbox" in form:
	query = form["searchbox"].value
	displayQuery = query
	query = query.strip()
#query = re.sub(r'\s+$', '', query) # remove trailing white spaces
	lange = form["langsel"].value
	#stop words
	stop = ['0','1','2','3','4','5','6','7','8','9','a','re','about', 'above', 'across', 'after', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'https','http','rt','co','always', 'among', 'an', 'and', 'another', 'any', 'anybody', 'anyone', 'anything', 'anywhere', 'are', 'area', 'areas', 'around', 'as', 'ask', 'asked', 'asking', 'asks', 'at', 'away', 'b', 'back', 'backed', 'backing', 'backs', 'be', 'became', 'because', 'become', 'becomes', 'been', 'before', 'began', 'behind', 'being', 'beings', 'best', 'better', 'between', 'big', 'both', 'but', 'by', 'c', 'came', 'can', 'cannot', 'case', 'cases', 'certain', 'certainly', 'clear', 'clearly', 'come', 'could', 'd', 'did', 'differ', 'different', 'differently', 'do', 'does', 'done', 'down', 'down', 'downed', 'downing', 'downs', 'during', 'e', 'each', 'early', 'either', 'end', 'ended', 'ending', 'ends', 'enough', 'even', 'evenly', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'f', 'face', 'faces', 'fact', 'facts', 'far', 'felt', 'few', 'find', 'finds', 'first', 'for', 'four', 'from', 'full', 'fully', 'further', 'furthered', 'furthering', 'furthers', 'g', 'gave', 'general', 'generally', 'get', 'gets', 'give', 'given', 'gives', 'go', 'going', 'good', 'goods', 'got', 'great', 'greater', 'greatest', 'group', 'grouped', 'grouping', 'groups', 'h', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'herself', 'high', 'high', 'high', 'higher', 'highest', 'him', 'himself', 'his', 'how', 'however', 'i', 'if', 'important', 'in', 'interest', 'interested', 'interesting', 'interests', 'into', 'is', 'it', 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kind', 'knew', 'know', 'known', 'knows', 'l', 'large', 'largely', 'last', 'later', 'latest', 'least', 'less', 'let', 'lets', 'like', 'likely', 'long', 'longer', 'longest', 'm', 'made', 'make', 'making', 'man', 'many', 'may', 'me', 'member', 'members', 'men', 'might', 'more', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', 'my', 'myself', 'n', 'necessary', 'need', 'needed', 'needing', 'needs', 'never', 'new', 'new', 'newer', 'newest', 'next', 'no', 'nobody', 'non', 'noone', 'not', 'nothing', 'now', 'nowhere', 'number', 'numbers', 'o', 'of', 'off', 'often', 'old', 'older', 'oldest', 'on', 'once', 'one', 'only', 'open', 'opened', 'opening', 'opens', 'or', 'order', 'ordered', 'ordering', 'orders', 'other', 'others', 'our', 'out', 'over', 'p', 'part', 'parted', 'parting', 'parts', 'per', 'perhaps', 'place', 'places', 'point', 'pointed', 'pointing', 'points', 'possible', 'present', 'presented', 'presenting', 'presents', 'problem', 'problems', 'put', 'puts', 'q', 'quite', 'r', 'rather', 'really', 'right', 'right', 'room', 'rooms', 's', 'said', 'same', 'saw', 'say', 'says', 'second', 'seconds', 'see', 'seem', 'seemed', 'seeming', 'seems', 'sees', 'several', 'shall', 'she', 'should', 'show', 'showed', 'showing', 'shows', 'side', 'sides', 'since', 'small', 'smaller', 'smallest', 'so', 'some', 'somebody', 'someone', 'something', 'somewhere', 'state', 'states', 'still', 'still', 'such', 'sure', 't', 'take', 'taken', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'therefore', 'these', 'they', 'thing', 'things', 'think', 'thinks', 'this', 'those', 'though', 'thought', 'thoughts', 'three', 'through', 'thus', 'to', 'today', 'together', 'too', 'took', 'toward', 'turn', 'turned', 'turning', 'turns', 'two', 'u', 'under', 'until', 'up', 'upon', 'us', 'use', 'used', 'uses', 'v', 'very', 'w', 'want', 'wanted', 'wanting', 'wants', 'was', 'way', 'ways', 'we', 'well', 'wells', 'went', 'were', 'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'whole', 'whose', 'why', 'will', 'with', 'within', 'without', 'work', 'worked', 'working', 'works', 'would', 'x', 'y', 'year', 'years', 'yet', 'you', 'young', 'younger', 'youngest', 'your', 'yours', 'z']
	#ch = form["check1"].checked
	#fullQuery = 'http://localhost:8983/solr/twitter/select?q='+ query + '+AND+http?+AND+lang%3Aen&wt=json&indent=true&rows=50'
	fp = 'http://localhost:8983/solr/twitter/select?q='
	for item in query:
		if item != " ":
			fp += item
		else:
			fp += "+AND+"
	rows = "1000"
	#if media is selected
	if "check1" in form:
		if lange == "NULL":
			fullQuery = fp +'+AND+http?&wt=json&indent=true&rows=10000'
		else:
			fullQuery =  fp + '+AND+http?+AND+lang%3A' + lange+'&wt=json&indent=true&rows=10000'
	else:
		if lange == "NULL":
			#http://localhost:8983/solr/twitter/select?q=Barcas&rows=1000&wt=json&indent=true
			fullQuery = fp +'&wt=json&indent=true&rows=10000'
		else:
			fullQuery =  fp + '+AND+lang%3A' + lange+'&wt=json&indent=true&rows=10000'
	# 'http://localhost:8983/solr/twitter/select?q=arsenal+AND+http?+AND+lang%3Aen&wt=json&indent=true&rows=50'
else:
	fullQuery = "http://localhost:8983/solr/twitter/select?wt=json&indent=true"
conn = urlopen(fullQuery)
#print(str(conn))
result_in_json = simplejson.load(conn)
links = {}
name = {}
pic = {}

#pp = pprint.PrettyPrinter(indent=2)
#print result_in_json
for hit in result_in_json['response']['docs']:
	#print i['text']
	#print hit['text']
	if hit['text'] == None:
		break	
	#if media is selected
	temp = None
	if "check1" in form:
		tempz = re.search( "(?P<url>https?://[^\s]+)",("".join(hit['text'] ) ).decode('utf-8') )
		if tempz != None:
			temp = tempz.group("url")
		if temp != None:
			temp1 = "".join(hit['text'])
			links[temp1] = temp
			ntemp = "".join(hit['screen_name'])
			name[temp1] = ntemp
			ptemp = "".join(hit['profile_image_url_https'])
			pic[temp1] = ptemp
	else:
		temp1 = "".join(hit['text'])
		links[temp1] = ""
		ntemp = "".join(hit['screen_name'])
		name[temp1] = ntemp
		ptemp = "".join(hit['profile_image_url_https'])
		pic[temp1] = ptemp

text = []
keydic = {}
for key in links:
	text.append(key)

for tweet in text:
	li = re.compile('\w+').findall(tweet)
	for word in li:
		if word.lower() in stop:
			continue
		if word not in keydic:
			keydic[word] = 1
		else:
			keydic[word] += 1
sorted_x = sorted(keydic.items(), key=operator.itemgetter(1),reverse = True )


print "Content-type:text/html\n\r\n\r" 
print "<html>"
print "<head><title>Display Links</title>"
print "<meta charset=\"utf-8\">"
print "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
print "<link href=\"bootstrap.min.css\" rel=\"stylesheet\" media=\"screen\">"
print "<link href=\"custom.css\" rel=\"stylesheet\" media=\"screen\">"
print "<link rel=\"stylesheet\" href=\"http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css\">"

print "<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js\"></script>"
print "<script src=\"http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js\"></script>"
print "</head>"
print "<body style=\"background-color: #ebeff0\">"

print " <div class=\"row\" style=\"background-color: white;\">"
print "  <div class=\"col-sm-3\">"
print "<br>"
print "<a href=\"../hardtackle\">"
print "<img src=\"../hardtackle/test.jpg\" class = \"center-block\" style=\"width: 250px; height: 97px;\" />"
print "</a>"
print "</div>"
print "  <div class=\"col-sm-6\">"
print "<br>"
print "<br>"
print "<form name=\"search\" action=\"y.cgi\" method=\"POST\">"
print "<input type=\"text\" id=\"sbox\" class=\"form-control no-radius\" name=\"searchbox\" autofocus>"
print "<br>"
print "<div class=\"col-sm-6\">"
print "<label class=\"checkbox-inline checkbox-success\"><input type=\"checkbox\" name = \"check1\" id =\"cb1\" value=\"unchecked\">Media Preference</label>"
print "</div>"
print "<div class=\"col-sm-6\">"
print "  <select name=\"langsel\" id=\"dd1\" class=\"form-control\">"
print "    <option value=\"NULL\">Language (Any)</option>"
print "    <option value=\"en\">English</option>"
print "    <option value=\"es\">Spanish</option>"
print "    <option value=\"fr\">French</option>"
print "  </select>"
print "</div>"
print "<script type=\"text/javascript\">"
print "function calc1()"
print "{"
print "	alert(document.getElementById('dd1').value);"
print "}"
print "</script>"
print "<script type=\"text/javascript\">"
print "$(\".dropdown-menu li a\").click(function(){"
print "  $(this).parents(\".dropdown\").find('.btn').html($(this).text() + ' <span class=\"caret\"></span>');"
print "  $(this).parents(\".dropdown\").find('.btn').val($(this).data('value'));"
print "});"
print "</script>"
print "<br>"
print "<br>"
print "<br>"
print "</div>"
print "<script>"
print "var checkbox = $(\"cb1\");"
print "checkbox.change(function(event) {"
print "    var checkbox = event.target;"
print "if (checkbox.checked) {"
print "      document.getElementById(\"cb1\").value = \"selected\" ;"
print "   } else {"
print "      document.getElementById(\"cb1\").value = \"unselected\";" 
print "    }"
print "});"
print "</script>"
print "  <div class=\"col-sm-3\"></div>"
print "<br>"
print "<br>"
print "<input type=\"submit\" id=\"submit_btn\" class=\"btn btn-success \" value=\"Search\" style=\"height:40px; width:160px\">"
print "</form> "
print "</div>"
print "<div class=\"row\">"
print "<div class=\"col-sm-3\">"
print "</div>"
print "<div class=\"col-sm-6\">"
print "<div class=\"col-sm-6\">"
print "<h4>Search Results: <font size=\"2\">" + str ( len(text) ) + " hits for " + displayQuery +  "</font></h4>"
pageCount = int ( math.ceil ( len( text ) / 20.0  ) )
print "</div>"
print "<div class=\"col-sm-6\">"
print "<h5 align=\"right\"> Page <label id=\"pageNo\">1</label></h5>"
print "</div>"
print "<table id = \"myTable\" class = \"table table-striped\"> "
counter = 0
for key in links:
	if key == None:
		break
	counter += 1
	if counter<=20:
		print "<tr>"
		print "<td style=\"display:1;\" width=\"50\"><a href = https://twitter.com/" + name[key] + "><img src=https://twitter.com/" + name[key] + "/profile_image height = \"50\" width = \"50\"></a></td>"
		print "<td style=\"display:1;\"><a href = https://twitter.com/" + name[key] + ">" +"@"+ name[key] + "</a>: " + key + "<br>" + " <a href=" + links[key] + ">" +  links[key] + "</a></td>"
		print "</tr>"
	else:
		print "<tr>"
		print "<td style=\"display:none;\" width=\"50\"><a href = https://twitter.com/" + name[key] + "><img src=https://twitter.com/" + name[key] + "/profile_image height = \"50\" width = \"50\"></a></td>"
		print "<td style=\"display:none;\"><a href = https://twitter.com/" + name[key] + ">" +"@"+ name[key] + "</a>: " + key + "<br>" + " <a href=" + links[key] + ">" +  links[key] + "</a></td>"
		print "</tr>"		
	#print "<td><a href=" + links[key] + ">"+ links[key] + "</a></td>"
print "</table>"
print "<div class=\"row\">"
print "&nbsp&nbsp&nbsp&nbsp&nbsp<input type=\"button\" class = \"btn btn-success\" onclick=\"changeContentBack()\" value=\"Prev\">"
print "&nbsp<input type=\"button\" class = \"btn btn-success\" onclick=\"changeContent()\" value=\"Next\">"
print "</div>"
print "<script type=\"text/javascript\">"
print "count =1;"
print "limit=" + str( pageCount ) + ";"

print "function changeContent(){"
print "if(count!=limit)"
print "count++;"
print "document.getElementById('pageNo').textContent = count;"
print "var x=document.getElementById('myTable').rows;"
print "var rows_len = document.getElementById('myTable').getElementsByTagName(\"tr\").length;"
print "for (i = 0; i < rows_len; i++) {"
print "	if(i < ((count-1)*20) || i>=(count*20))"
print "		{"
print "			var y=x[i].cells;"
print "			y[0].style = \"display:none\";"
print "			y[1].style = \"display:none\";"
print "		}"
print "	else"
print "		{"
print "			var y=x[i].cells;"
print "			y[0].style = \"display:1\";"
print "			y[1].style = \"display:1\";"
print "		}"
print "}"
print "}"

print "function changeContentBack(){"
print "if(count!=1)"
print "count--;"
print "document.getElementById('pageNo').textContent = count;"
print "var x=document.getElementById('myTable').rows;"
print "var rows_len = document.getElementById('myTable').getElementsByTagName(\"tr\").length;"
print "for (i = 0; i < rows_len; i++) {"
print "	if(i < ((count-1)*20) || i>=(count*20))"
print "		{"
print "			var y=x[i].cells;"
print "			y[0].style = \"display:none\";"
print "			y[1].style = \"display:none\";"
print "		}"
print "	else"
print "		{"
print "			var y=x[i].cells;"
print "			y[0].style = \"display:1\";"
print "			y[1].style = \"display:1\";"
print "		}"
print "}"
print "}"
print "</script>"

print "</div>"
print "<div class=\"col-sm-3\">"
print "<h5>Suggested Searches:</h5>"
if len( sorted_x ) < 10:
	for item in sorted_x:
		print "<a href=\"#\"><label onclick=\"do1(this);\">" + item[0] + "</label></a><br>"
else:
	for num in range(10):
		print "<a href=\"#\"><label onclick=\"do1(this);\">" + sorted_x[num][0] + "</label></a><br>"

print "</div>"
print "<script type=\"text/javascript\">"
print "function do1(id1)"
print "{"
print "	document.getElementById('sbox').value = id1.textContent"
print "	document.getElementById('submit_btn').click();"
print "}"
print "</script>"
print "</div>"
print "</body>"
print "</html>"
