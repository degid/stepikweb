from django.conf.urls import url
from qa.views import test

urlpatterns = [
    url(r'^question/(\d+)/$', test, name='question'),
    #url(r'admin/', admin.site.urls),
]
