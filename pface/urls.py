from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('pface.views',
    url(r'^$', 'printer', name='printer'),
    url(r'^gcode/rm/(?P<id>\d+)/', 'rmgcode', name='rmgcode'),
    url(r'^printer/command/', 'command', name='command'),
)