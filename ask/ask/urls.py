from django.conf.urls import include, url
from qa.views import test, index, popular, question

urlpatterns = [
    url(r'^$', index),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^ask/$', test),
    url(r'^popular/$', popular),
    url(r'^new/$', test),
    url(r'^question/', include('qa.urls')),
]
