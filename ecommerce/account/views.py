import random

from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from PIL import Image
from dashboard.models import *
from main.models import *
from product.models import *
from product.views import get_data_cart
from .forms import _customers, _state, _city ,_address
from .models import *
import os
# Create your views here.
@api_view(['POST'])
def return_code(request):
    phonenumber = request.data.get('number_phone') or None
    request.session['phonenumber'] = phonenumber
    code = random.randint(100000, 999999)
    request.session['otp'] = code
    print(code)
    text = 'کد به شماره تماس {} ارسال شد'.format(phonenumber) if phonenumber else 'شماره نامعتبر'
    return Response({
        'text':text
    })
def create_account(request):
    if request.method == "POST":
        form = _customers(request.POST)
        if request.POST.get('phone_number') == request.session['phonenumber'] and int(request.POST.get('otp')) == request.session['otp']:
            if form.is_valid():
                form.save()
                del request.session['phonenumber']
                del request.session['otp']
                user = authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
                login(request, user)
                return redirect('index')
            else:
                return redirect('index')
        else:
            return redirect('index')
@login_required
def profile(request):
    ins = get_object_or_404(customers, id=request.user.id)
    form = _customers(instance=ins)
    if request.method == "POST":
        if request.POST.get('email') and request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('phone_number') :
            ins.email = request.POST.get('email')
            ins.username = request.POST.get('email')
            ins.first_name = request.POST.get('first_name')
            ins.last_name = request.POST.get('last_name')
            try:
                if len(request.FILES['image']) != 0:
                    Image.open(request.FILES['image'])
                    if ins.image:
                        os.remove(ins.image.path)
                    ins.image = request.FILES['image']
            except:
                pass
            ins.save()
            if ins.phone_number != request.POST.get('phone_number'):
                request.session['phonenumber'] = request.POST.get('phone_number')
                code = int(random.randint(100000, 999999))
                request.session['otp'] = code
                print(code)
                return redirect('phone_number_change')
            return redirect('profile')
    valtreemenu = treemenu.objects.all() or False
    valmenu = menu.objects.all() or False
    valsubmenu = submenu.objects.all() or False
    valsub_footer = sub_footer.objects.all() or False
    valmain_footer = main_footer.objects.all() or False
    logo = logo_site.objects.all() or False
    icon = icon_site.objects.all() or False
    valcategory = subcategory.objects.filter(showindexpage = 1) or False
    valnavbar = navbar_process.objects.all() or False
    valswiper = swiper.objects.all() or False
    content = {
        'form' : form,
        'valtreemenu': valtreemenu,
        'valmenu': valmenu,
        'valsubmenu': valsubmenu,
        'valsub_footer': valsub_footer,
        'valmain_footer': valmain_footer,
        'logo': logo,
        'icon': icon,
        'valcategory': valcategory,
        'valnavbar': valnavbar,
        'valswiper': valswiper,
    }
    return render(request, 'main/account-overview.html',content)
def change_phone_number(request):

    if request.session['phonenumber']:
        if request.method == "POST":
            if int(request.POST.get('otp')) == request.session['otp']:
                ins = get_object_or_404(customers, id=request.user.id)
                ins.phone_number = request.session['phonenumber']
                ins.save()
                return redirect('profile')
        return render(request, 'main/change-mobile.html' )
    else:
        return redirect('profile')
def change_password(request):
    form = PasswordChangeForm(request.user)
    if request.method == "POST":
        form = PasswordChangeForm(request.user ,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('profile')
        else:
            messages.error(request,'پسورد فعلی شما ویا پسورد جدید با هم مطابقت ندارد')
    content = {
        'form': form,
    }
    return render(request, 'main/account-security.html', content)
def state_manager(request):
    datas = state.objects.all()
    if request.method == "POST":
        form = _state(request.POST , instance=state.objects.get(pk=request.POST.get('state-id'))) if request.POST.get('state-id') else _state(request.POST)
        if form.is_valid():
            form.save()
            return redirect('state')
        else:
            content = {
                'form': form,
                'datas': datas,
                'title': 'استان ها',
            }
            return render(request, 'dashboard/state.html', content)
    form = _state()
    content = {
        'form' : form ,
        'datas' : datas ,
        'title' : 'استان ها' ,
    }
    return render(request, 'dashboard/state.html' , content)
@api_view(['GET'])
def _update_state(request):
    ins = get_object_or_404(state , id = request.GET.get('data'))
    text = {'id': ins.id, 'title': ins.title}
    return Response({
        'text' : text,
    })
def _delete_state(request , id_state):
    ins = get_object_or_404(state,id = id_state)
    ins.delete()
    return redirect('state')
def city_manager(request):
    datas = city.objects.all()
    if request.method == "POST":
        form = _city(request.POST , instance=city.objects.get(pk=request.POST.get('city-id'))) if request.POST.get('city-id') else _city(request.POST)
        if form.is_valid():
            form.save()
            return redirect('city')
        else:
            content = {
                'form': form,
                'datas': datas,
                'title': 'شهر ها',
            }
            return render(request, 'dashboard/city.html', content)
    form = _city()
    context = {
        'title' : 'شهر ها',
        'form' : form,
        'datas' : datas,
    }
    return render(request, 'dashboard/city.html',context)
@api_view(['GET'])
def _update_city(request):
    ins = get_object_or_404(city , id = request.GET.get('data'))
    text = {'id': ins.id, 'state': ins.state.id, 'title': ins.title}
    return Response({
        'text' : text,
    })
def _delete_city(request , id_city):
    ins = get_object_or_404(city,id = id_city)
    ins.delete()
    return redirect('city')
def manage_address(request):
    valtreemenu = treemenu.objects.all() or False
    valmenu = menu.objects.all() or False
    valsubmenu = submenu.objects.all() or False
    valsub_footer = sub_footer.objects.all() or False
    valmain_footer = main_footer.objects.all() or False
    logo = logo_site.objects.all() or False
    icon = icon_site.objects.all() or False
    valcategory = subcategory.objects.filter(showindexpage=1) or False
    valnavbar = navbar_process.objects.all() or False
    valswiper = swiper.objects.all() or False
    addresses = address.objects.filter(user = request.user.id) or False
    cities = city.objects.all()
    content = {
        'valtreemenu': valtreemenu,
        'valmenu': valmenu,
        'valsubmenu': valsubmenu,
        'valsub_footer': valsub_footer,
        'valmain_footer': valmain_footer,
        'logo': logo,
        'icon': icon,
        'valcategory': valcategory,
        'valnavbar': valnavbar,
        'valswiper': valswiper,
        'addresses': addresses,
        'cities': cities,
    }
    if request.method == "POST":
        form = _address(request.POST , instance=address.objects.get(pk=request.POST.get('address-id'))) if request.POST.get('address-id') else _address(request.POST)
        if form.is_valid():
            form.save()
            return redirect('address')
        else:
            return render(request, 'main/account-address.html', content)
    return render(request , 'main/account-address.html',content)
@api_view(['GET'])
def update_address(request):
    ins = get_object_or_404(address , id = request.GET.get('data'))
    text = {'id' : ins.id , 'title':ins.title,'city':ins.city.id,'description':ins.description,'zipcode':ins.zipcode}
    return Response({
        'text' : text
    })
@login_required
def manage_orders(request):
    carts = cart.objects.filter(user=request.user or False)
    order = orders.objects.filter(user=request.user or False)
    addresses = address.objects.filter(user = request.user.id) or False
    payments = payment.objects.filter(user = request.user.id,status=100) or False
    other_payments = payment.objects.filter(user = request.user.id,status__lt=100) or False
    pl = False
    price = False
    if carts:
        pl = []
        [pl.append(x.pro.return_cart(x.pri.show_price(request), x.count,x.pri_id)) for x in carts]
        price = sum([x['price'] * x['count'] for x in pl])
    context = {
        'carts' : carts,
        'order' : order,
        'pl' : pl,
        'price' : price,
        'addresses' : addresses,
        'payments' : payments,
        'other_payments' : other_payments,
    }
    return render(request , 'main/account-orders.html' , context)
def view_login(request):
    a = request.POST
    user = authenticate(request, username=a.get('email'), password=a.get('password'))
    if user is None:
        return redirect('index')
    else:
        login(request, user)
        return redirect('profile')
def view_logout(request):
    logout(request)
    return redirect('index')