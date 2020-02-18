from django.conf.urls import url
from .views import PlaylistView

urlpatterns = [
    url(r'^$', PlaylistView.as_view(), name='playlist'),
]