from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^student_list/$', views.StudentList),
    url(r'^student_detail/(?P<pk>[0-9]+)$', views.StudentDetail),
]

urlpatterns = format_suffix_patterns(urlpatterns)