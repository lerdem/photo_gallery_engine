import datetime
from django.shortcuts import render
from django.http import HttpResponse


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
