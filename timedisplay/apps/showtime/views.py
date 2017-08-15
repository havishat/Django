
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
  context = {
  "time": strftime("%b %d, %Y %H:%M %p", gmtime())
  }
  return render(request,'showtime/index.html', context)

