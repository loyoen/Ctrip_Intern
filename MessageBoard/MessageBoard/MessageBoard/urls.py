from django.conf.urls import include, url
from django.contrib import admin
import settings
from Board.views import *
urlpatterns = [
    url(r'^$', index),
    url(r'^toWrite/$', toWrite),
    url(r'^publish/$', publish),
    url(r'^blog/(?P<blog_id>\d+)/$$', browse),
    url(r'^delete/$', delete),
    url(r'^correctData/(?P<blog_id>\d+)/$$', correctData),
    url(r'^modify/$', modify),
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
]

