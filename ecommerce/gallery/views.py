import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.clickjacking import xframe_options_exempt

from .models import images
# Create your views here.
def upload_images(request):
    if request.method == "POST":
        if request.FILES:
            i = images.objects.create()
            i.image = request.FILES['file']
            i.save()
    return render(request, 'dashboard/images.html')
def show_images(request):
    datas = images.objects.all() or False
    content = {
        'title': "نمایش عکس ها ",
        'datas' : datas,
        'datas2' : datas,
    }
    return render(request, 'dashboard/show_images.html' , content)
def update_images(request):
    if request.method == 'POST':
        i = images.objects.get(id = int(request.POST.get('imageid')))
        i.alt = request.POST.get('alt')
        i.save()
        return JsonResponse({'data': i.pk})
def del_images(request):
    if request.method == 'POST':
        i = images.objects.get(id = int(request.POST.get('imageid')))
        os.remove(i.image.path)
        i.delete()
        return JsonResponse({'data': 'ok'})
@xframe_options_exempt
def select_image(request):
    datas = images.objects.all() or False
    content = {
        'title': "نمایش عکس ها ",
        'datas': datas,
        'datas2': datas,
    }
    return render(request, 'dashboard/select_image.html', content)
@xframe_options_exempt
def select_multi_image(request):
    datas = images.objects.all() or False
    content = {
        'title': "نمایش عکس ها ",
        'datas': datas,
        'datas2': datas,
    }
    return render(request, 'dashboard/select_multi_image.html', content)