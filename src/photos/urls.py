from django.conf.urls import url

from photos import views

urlpatterns = [
    url(r'^home/', views.PhotoListView.as_view(), name='home'),
    url(r'voice/add/', views.add_voice, name='add-voice'),
    url(r'voice/(<int:id>)/$', views.get_voice, name='get-voice'),
]
