from django.shortcuts import HttpResponse
import os

def home(request):
	print(os.environ.get('MSG'))
	return HttpResponse("Home page.")