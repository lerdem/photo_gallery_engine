from django.conf.urls import url

from photos import views

urlpatterns = [
    url(r'^home/', views.PhotoListView.as_view(), name='home'),
    url(r'add-voice/', views.add_voice, name='add-voice'),
    url(r'get-voice-class-status/', views.get_voice, name='get-voice-class-status'),
]
