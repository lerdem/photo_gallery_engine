from django.conf.urls import url, include
from rest_framework import routers

from photos import views

router = routers.DefaultRouter()
router.register(r'photos', views.PhotoViewSet)


apipatterns = [
    url(r'^', include(router.urls)),
]

urlpatterns = [
    url(r'^home/', views.PhotoListView.as_view(), name='home'),
    url(r'add-voice/', views.add_voice, name='add-voice'),
    url(r'get-voice-class-status/', views.get_voice, name='get-voice-class-status'),
]

urlpatterns += apipatterns