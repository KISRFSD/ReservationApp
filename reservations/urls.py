from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'eventHome.views.index', name='home'),
     url(r'^regtrip/$', 'eventHome.views.regtrip', name='regtrip'),
     url(r'^feedback/$', 'feedback.views.feed', name='feedback'),
     url(r'^signup/$', 'eventHome.views.signup', name='signup'),
     # url(r'^blog/', include('blog.urls')),
     url(r'^feedback/$', 'feedback.views.feed', name='feedback'),
     url(r'^admin/', include(admin.site.urls)),
)
