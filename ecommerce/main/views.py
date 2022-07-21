import random

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import os
from django.db.models import Q
from django.utils.formats import number_format
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.utils import json

from account.forms import _customers
from .forms import *
from dashboard.models import *
from product.models import *


# Create your views here.
from .serializers import return_data_logo, return_data_icon, return_data_treemenu, return_data_menu, \
    return_data_submenu, return_data_subfooter, return_data_mainfooter, return_product, return_data_subcategory


def index(request):
    x = viewsite.objects.get(id = 1)
    x.addview()
    valsub_footer = sub_footer.objects.all() or False
    valmain_footer = main_footer.objects.all() or False
    valbrand = brand.objects.filter(showindexpage = 1) or False
    valproduct = product.objects.filter(visibility = 1) or False
    valcategory = subcategory.objects.filter(showindexpage = 1) or False
    valnavbar = navbar_process.objects.all() or False
    valswiper = swiper.objects.all() or False
    valblog = blogs.objects.all() or False
    customers = _customers()
    content = {
        'valsub_footer' : valsub_footer,
        'valmain_footer' : valmain_footer,
        'valbrand' : valbrand,
        'valproduct' : valproduct,
        'valcategory' : valcategory,
        'valnavbar' : valnavbar,
        'valswiper' : valswiper,
        'valblog' : valblog,
        'customers' : customers,
    }
    return render(request , 'main/index.html' , content)
def page_show(request,pagename):
    pagename = slugify(pagename, allow_unicode=True)
    data = get_object_or_404(page_generator,url=pagename)
    content = {
        'data': data,
    }
    return render(request, 'main/page.html', content)
def set_logo(request):
    if request.method == "POST":
        if request.POST.get('image_id'):
            ins = get_object_or_404(logo_site,pk = request.POST.get('image_id'))
            if request.FILES.get('image', False):
                os.remove(ins.image.path)
            form = logo_site_(request.POST, request.FILES, instance=ins)
        else:
            form = logo_site_(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            redirect('set_logo')
        else:
            data = logo_site.objects.all()
            content = {
                'title': 'ست کردن لوگوی سایت',
                'data': data,
                'form': form,
            }
            return render(request, 'dashboard/logo.html', content)
    data = logo_site.objects.all() or False
    form = logo_site_(initial={'title': data.first().title })
    content = {
        'title' : 'ست کردن لوگوی سایت',
        'data' : data,
        'form' : form,
    }
    return render(request, 'dashboard/logo.html' , content)
def set_icon(request):
    if request.method == "POST":
        if request.POST.get('icon_id'):
            ins = get_object_or_404(icon_site, pk=request.POST.get('icon_id'))
            os.remove(ins.image.path)
            form = icon_site_(request.POST, request.FILES, instance=ins)
        else:
            form = icon_site_(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('set_icon')
        else:
            data = icon_site.objects.all()
            content = {
                'title': 'ست کردن آیکون سایت',
                'data': data,
                'form': form,
            }
            return render(request, 'dashboard/icon.html', content)
    form = icon_site_()
    data = icon_site.objects.all() or False
    content = {
        'title': 'ست کردن آیکون سایت',
        'data': data,
        'form': form,
    }
    return render(request, 'dashboard/icon.html', content)
def blog_list(request):
    filter = request.GET.get('filter', False)
    if filter:
        set_filter = '{%s}' % filter
        set_filter = json.loads(set_filter)
        valblogs = blogs.objects.filter(**set_filter) or False
    else:
        valblogs = blogs.objects.all() or False
    valbrand = brand.objects.filter(showindexpage = 1) or False
    valproduct = product.objects.filter(visibility = 1) or False
    valcategory = subcategory.objects.filter(showindexpage = 1) or False
    valnavbar = navbar_process.objects.all() or False
    valswiper = swiper.objects.all() or False

    valblogcategory = category_blog.objects.all() or False
    content = {
        'valbrand': valbrand,
        'valproduct': valproduct,
        'valcategory': valcategory,
        'valnavbar': valnavbar,
        'valswiper': valswiper,
        'valblogs': valblogs,
        'valblogcategory': valblogcategory,

    }
    return render(request, 'main/blog-list.html' , content)
def blog(request,title):
    valblog=get_object_or_404(blogs,url=title)
    valnavbar = navbar_process.objects.all() or False
    valswiper = swiper.objects.all() or False
    valblogs = blogs.objects.all() or False
    content = {
        'valnavbar': valnavbar,
        'valswiper': valswiper,
        'valblogs': valblogs,
        'valblog': valblog,
    }
    return render(request, 'main/blog.html',content)
@api_view(['GET'])
def return_header(request):
    logo = logo_site.objects.first() or False
    icon = icon_site.objects.first() or False
    valtreemenu = treemenu.objects.all() or False
    valmenu = menu.objects.all() or False
    valsubmenu = submenu.objects.all() or False
    valsubcategory = subcategory.objects.all() or False
    slogo = return_data_logo(logo,many=False)
    sicon = return_data_icon(icon,many=False)
    streemenu = return_data_treemenu(valtreemenu,many=True)
    smenu = return_data_menu(valmenu,many=True)
    ssubmenu = return_data_submenu(valsubmenu,many=True)
    ssubcategory = return_data_subcategory(valsubcategory,many=True)
    datas = {'logo' : slogo.data,'icon' : sicon.data,'treemenu':streemenu.data,'menu':smenu.data,'submenu' : ssubmenu.data,'subcategory' : ssubcategory.data}
    return Response(datas)
@api_view(['GET'])
def return_footer(request):
    valsub_footer = sub_footer.objects.all() or False
    valmain_footer = main_footer.objects.all() or False
    sub = return_data_subfooter(valsub_footer, many=True)
    main = return_data_mainfooter(valmain_footer, many=True)
    datas = {'sub': sub.data, 'main': main.data,}
    return Response(datas)

@api_view(['POST'])
def send_forgot_code(request):
    try :
        phonenumber = request.data.get('number_phone')
        request.session['phonenumber'] = phonenumber
        user = customers.objects.get(phone_number= phonenumber)
        code = random.randint(100000, 999999)
        request.session['otp'] = code
        text ='کد شما {} می باشد' .format(code)
    except:
        text =  'چنین شماره ای ثبت نشده است'
    return Response({
        'text' : text,
    })
def view_reset_passwd(request):
    return render(request, 'main/forgot-password.html')
@api_view(['POST'])
def setpassword(request):
    otp = request.data.get('otp')
    pass1 = request.data.get('pass1')
    pass2 = request.data.get('pass2')
    if int(otp) == int(request.session['otp']) and len(pass1) >= 8 and pass1 == pass2:
        try :
            user = customers.objects.get(phone_number= request.session['phonenumber'])
            user.password = make_password(pass1)
            update_session_auth_hash(request, user)
            text = 'ok'
        except:
            text = 'لطفا از صحت کد تایید و پسورد ها اطمینان حاصل فرمایید'
    else:
        text = 'لطفا از صحت کد تایید و پسورد ها اطمینان حاصل فرمایید'
    return Response({
        'text' : text,
    })
@api_view(['POST'])
def search(request):
    sea = request.data.get('text')
    searchpro = product.objects.filter(Q(name__icontains=sea) | Q(engname__icontains=sea))[:5]
    result = return_product(searchpro,many=True)
    return Response({'text' :result.data})
@api_view(['POST'])
def set_image(request):
    searchimage = images.objects.get(id = request.data.get('text'))
    return Response({'url' :searchimage.image.url})
