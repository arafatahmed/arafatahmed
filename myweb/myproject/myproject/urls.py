#from django.conf.urls import include, url
from django.urls import include, re_path as url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('main.urls'))
]
