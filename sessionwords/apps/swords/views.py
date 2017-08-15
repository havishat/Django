
# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
  # the index function is called when root is visited
def index(request):
  return render(request,'swords/index.html')

def add_word(request): 
  # if request.method == "POST":
  #   request.session['word'] = request.POST['word']
  new_word = {}
  for key, value in request.POST.iteritems():
    if key != "bigfont":
        new_word[key] = value
    if key == "bigfont":
        new_word['bigfont'] = "bigfont"
    else:
        new_word['bigfont'] = ""
  new_word['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")

try:
    request.session['words']
  except KeyError:
    request.session['words'] = []

  temp_list = request.session['words']
  temp_list.append(new_word)
  request.session['words'] = temp_list
  return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

