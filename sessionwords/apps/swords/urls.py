from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^surveys/add_word$', views.add_word),  
    url(r'^surveys/clear$', views.clear),    
]
