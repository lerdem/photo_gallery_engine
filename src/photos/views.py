import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.views import View


from photos import models
from photos import forms


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


class PhotoListView(ListView):

    queryset = models.Photo.objects.all().order_by('-created')


class VoiceAdd(View):
    form_class = forms.VoiceForm
    template_name = 'photos/voice_form.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            # <process form cleaned data>
            # after test add redirect
            # add signal to count voices and return update num
            return HttpResponse('success blah')

        return render(request, self.template_name, {'form': form})