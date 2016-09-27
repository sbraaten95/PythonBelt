from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^poke/(?P<id>\d+)$', views.poke, name='poke'),
    url(r'^logout$', views.logout, name='logout')
]