from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sandeep(request):
    s="<h1> Hello This is first project and this is nursery level </h1>"
    return HttpResponse(s)