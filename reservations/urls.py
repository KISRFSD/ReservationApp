from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'eventHome.views.index', name='home'),
     url(r'^feedback/$', 'eventHome.views.feedback', name='Feedback'),
     url(r'^signup/$', 'eventHome.views.signup', name='Signup'),
     url(r'^regtrip/$', 'eventHome.views.regtrip', name='RegTrip'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
