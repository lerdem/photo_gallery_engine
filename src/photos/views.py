import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView


from photos import models


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


class PhotoListView(ListView):

    # model = models.Photo
    queryset = models.Photo.objects.all().order_by('-created')
