from django.conf.urls import url
from .views import SocialView

urlpatterns = [
    url(r'^$', SocialView.as_view(), name='social'),
]