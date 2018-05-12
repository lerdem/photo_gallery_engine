from django.conf.urls import url

from photos import views

urlpatterns = [
    url(r'^time/', views.current_datetime),
    url(r'^home/', views.PhotoListView.as_view()),
]
