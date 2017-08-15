# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from __future__ import unicode_literals
import random
import string
from django.shortcuts import render, redirect

def randomword(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

# Create your views here.
def index(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0

    return render(request, "randomword/index.html")

def generate(request):
    request.session['tries'] += 1  
    request.session['word'] = randomword(10)
    return redirect('/')

def reset(request):
  try: 
    del request.session['tries']
    # del request.session['word']
  except KeyError:
    del request.session['tries']
  return redirect('/')