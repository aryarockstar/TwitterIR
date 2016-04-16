# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	#now = "Seven"
    	#html = "<html><body>It is now %s.</body></html>" % now
    	#return HttpResponse(html)
	return render(request, "index.html", {})
