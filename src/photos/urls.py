from django.conf.urls import url

from photos.views import current_datetime

urlpatterns = [
    url(r'^time/', current_datetime),
]
