from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage' : "I am bold message"}
	return render(request,'rango/index.html',context_dict)
def about(request):
	return HttpResponse("Rango says hey there about")