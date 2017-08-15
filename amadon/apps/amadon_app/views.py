# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    items = [{ "value":1, "name": "Dojo Tshirt", "price": 19.99},{"value":2,  "name": "Dojo Sweater", "price": 29.99},{"value":3, "name": "Dojo Cup", "price": 4.99},{"value":4,  "name": "Algorithm Book", "price":49.99}]
    itemsx = {
            "items":items
    }
    # print request.POST['quantity']
    # if  request.POST.get['quantity'] > 0 :
    #     for key, value in items.iteritems():
    #         if key == "price":
    #             request.session['price'] 
    try:
        request.session['number_of_items'] 
    except KeyError:
        request.session['number_of_items'] = 0
    try:
        request.session['total_cost']
    except KeyError:
        request.session['total_cost'] = 0
    return render(request,'amadon_app/index.html',itemsx)

def results(request):
    
    x = float(request.POST['price'])
    y = float(request.POST['quantity'])
    request.session['total'] = x * y
    print request.session['total']
    request.session['number_of_items'] += y 
    request.session['total_cost'] += request.session['total']
    return redirect("/amadon_app/checkout")

def checkout(request):
	return render(request,'amadon_app/results.html')

def clear(request):
	request.session.clear()
	return redirect('/')