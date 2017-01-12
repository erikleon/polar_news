from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^latest/', views.latest, name='latest'),
    url(r'^query_polar/', views.query_polar, name='query_polar'),
    url(r'^build/', views.build, name='latest'),
]
