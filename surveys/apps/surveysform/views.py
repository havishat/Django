# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
    request.session['count'] = 0 
    return render(request,'surveysform/index.html')

def process(request): 
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['Language']
        request.session['comment'] = request.POST['comment']
    return redirect('/results')
 
def results(request):
    request.session['count'] += 1
    print request.session['count']
    return render(request, "surveysform/results.html")
