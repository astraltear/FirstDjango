from django.conf.urls import patterns, include, url
from django.contrib import admin
import poll.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FirstDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^poll/list$', poll.views.list),
    url(r'^poll/choice/(?P<poll_id>\d+)/$', poll.views.choice),
)
