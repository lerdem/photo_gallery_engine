from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets


from photos import models
from photos import serializers


class PhotoListView(ListView):

    queryset = models.Photo.objects.all().order_by('-created')



def add_voice(request):

    if not request.session.session_key:
        request.session.cycle_key()
    # {id: 0/1}
    photo_id = request.GET['photo_id']
    key = f'voice_added_photos_{photo_id}'
    if key in request.session:
        if request.session[key]:
            request.session[key] = 0
            inc = -1
        else:
            request.session[key] = 1
            inc = 1
    else:
        request.session[key] = 1
        inc = 1
    result = 0

    # it has to return managet obj
    p = models.Photo.objects.filter(id=photo_id)

    inc_counter = p.last().counter + inc
    p.update(counter=inc_counter)
    result = inc_counter
    return JsonResponse({'res': result})


def get_voice(request):
    photo_ids = models.Photo.objects.all().values_list('id', flat=True)

    def check_img_class_status(photo_id):
        key = f'voice_added_photos_{photo_id}'
        class_img_status = 0

        if key in request.session:
            if request.session[key]:
                class_img_status = 1
        return class_img_status

    result = {photo_id: check_img_class_status(photo_id) for photo_id in photo_ids}

    return JsonResponse({'res': result})


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer
