from django.conf.urls import patterns, url
from .views import diver_list, diver_add

urlpatterns = patterns('',
                       url(r'^list/$', diver_list, name="diver_list"),
                       url(r'^add/$', diver_add),
                       )