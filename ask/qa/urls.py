from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^$', 'views.test'),
    url(r'^login/$', 'views.test'),
    url(r'^signup/$', 'views.test'),
    url(r'^question/\d+$', 'views.test'),
    url(r'^ask/$', 'views.test'),
    url(r'^popular/$', 'views.test'),
    url(r'^new/$', 'views.test'),
    #url(r'^admin/', admin.site.urls),
]
