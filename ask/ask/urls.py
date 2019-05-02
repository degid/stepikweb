from django.conf.urls import include, url
from qa.views import test, index, popular, question, ask, login_view, signup

urlpatterns = [
    url(r'^$', index),
    url(r'^login/$', login_view),
    url(r'^signup/$', signup),
    url(r'^ask/$', ask),
    url(r'^popular/$', popular),
    url(r'^new/$', test),
    url(r'^question/', include('qa.urls')),
]
