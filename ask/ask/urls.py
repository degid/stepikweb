from django.conf.urls import include, url
from qa.views import test

urlpatterns = [
    url(r'^$', test),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^ask/$', test),
    url(r'^popular/$', test),
    url(r'^new/$', test),
    url(r'^question/$', test),   
]
