from django.shortcuts import render
from django.http import HttpResponse
from bloceanapp.models import Lounge
import json

# Create your views here.


def lounge(request):
	locationrequest=request.GET.get('location')
	# if (Lounge.objects.all()[0].identifier==namerequest):
	# 	print "yes"
	#print responseDict
	queryDict=Lounge.objects.filter(location=locationrequest).values()
	print len(queryDict)
	responseDict={}
	for i in range(len(queryDict)):
		responseDict["%d"%(i+1)]=queryDict[i]

	jsonResponse=json.dumps(responseDict,indent=4)
	return HttpResponse(jsonResponse,content_type="application/json")

def adminPanel(request):
	return render(request,'bloceanapp/index.html')


