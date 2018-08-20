from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from myApi import urls
from myApi import views
urlpatterns = [
    path('',views.index),
    path('ajax',views.spitData),
    path('admin/', admin.site.urls),
    path('', include(urls)),
]
