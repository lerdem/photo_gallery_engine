from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.views import View
from django.core.exceptions import ObjectDoesNotExist


from photos import models
from photos import forms


class PhotoListView(ListView):

    queryset = models.Photo.objects.all().order_by('-created')


# def add_voice(request, photo_id, counter):
#     if request.POST:
#         form = forms.VoiceForm(request.POST)
#         if form.is_valid():
#             # form = form.save(commit=False)
#             photo_id = int(request.POST['photo'])
#             voice, created = models.Voice.objects.get_or_create(
#                 photo=photo_id,
#                 counter=1
#             )
#             result = voice.counter
#             if not created:
#                 voice.counter+=1
#                 result = voice.counter
#                 voice.save()
#             return JsonResponse({'status': result})
#         return JsonResponse({'status': form.errors})


def add_voice(request):

    # if not request.session.session_key:
    #     request.session.cycle_key()
    # request.session['add_voice'] = 1
    photo_id = request.GET['photo_id']
    counter = request.GET['counter']
    result = 0
    try:
        voice = models.Voice.objects.get(id=photo_id)
    except ObjectDoesNotExist:
        voice = None
    if voice:
        inc_counter = voice.counter + 1
        voice.update(counter=inc_counter)
        result = inc_counter
    else:
        photo = models.Photo.objects.get(photo_id)
        voice = models.Voice.objects.create(
            photo=photo,
            counter=1
        )
        result = 1
    return JsonResponse({'res': result})


def get_voice(request, id):
    queryset = 0
    result = {'status': 'error'}
    try:
        queryset = models.Voice.objects.get(id=id)
    except ObjectDoesNotExist:
        print('No')

    if queryset:
        result['status'] = 'success'
        result.update({'data': queryset.counter})
    return JsonResponse(result)