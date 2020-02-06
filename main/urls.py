from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.artist, name='artist'),
    url(r'^artist/(?P<pk>[0-9]+)/$', views.artist_info, name='artist_info'),
]