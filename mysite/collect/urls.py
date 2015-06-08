from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /collect/
    url(r'^$', views.index, name = 'index'),
    # ex: /1/vote/
    url(r'^(?P<query_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
