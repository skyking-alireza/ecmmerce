import os
import statistics
import json
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from account.models import cart
from dashboard.models import *
from main.models import *
from product.models import *
from product.models import subcategory
from product.forms import *
from gallery.models import images
from jalali_date import datetime2jalali, date2jalali
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.http import HttpResponseNotFound
def manage_main_category(request):
    datas = maincategory.objects.all() or False
    form = main_category()
    content = {
        'title':  "مدیریت محصولات",
        'form': form,
        'datas': datas,
        }
    return render(request , "dashboard/maincategory.html" , content)
@api_view(['POST'])
def deletemaincategory(request):
    try:
        vmaincategory = maincategory.objects.get(id = request.data.get('id'))
        vmaincategory.delete()
        return Response({'text': 'ok'})
    except:
        return Response({'text': 'bad'})
@api_view(['POST'])
def setmaincategory(request):
    try:
        if request.data.get('id'):
            vmaincategory = maincategory.objects.get(id = request.data.get('id'))
            vmaincategory.name= request.data.get('name')
            vmaincategory.descriptions = request.data.get('descriptions')
            vmaincategory.tags = request.data.get('tags')
            vmaincategory.keywords = request.data.get('keywords')
            vmaincategory.save()
            return Response({'text': 'ok','id' :request.data.get('id') })
        else:
            vmaincategory = maincategory.objects.create(name = request.data.get('name'),descriptions = request.data.get('descriptions'),tags=request.data.get('tags'),keywords=request.data.get('keywords'))
            return Response({'text': 'ok','idv':vmaincategory.id})
    except:
        return Response({'text': 'bad'})
def manage_sub_category(request, subcategory=subcategory):
    form = sub_category()
    subcategory = subcategory.objects.all()
    select_images = images.objects.all()
    content = {
        'title': "مدیریت محصولات",
        'select_images': select_images,
        'form': form,
        'datas': subcategory,
    }
    return render(request, "dashboard/subcategory.html", content)
@api_view(['POST'])
def deletesubcategory(request):
    try:
        vsubcategory = subcategory.objects.get(id = request.data.get('id'))
        vsubcategory.delete()
        return Response({'text': 'ok'})
    except:
        return Response({'text': 'bad'})
@api_view(['POST'])
def setsubcategory(request):
    try:
        if request.data.get('id'):
            vsubcategory = subcategory.objects.get(id = request.data.get('id'))
            vsubcategory.name = request.data.get('name')
            vsubcategory.category_id = request.data.get('category')
            vsubcategory.showindexpage = request.data.get('showindexpage')
            vsubcategory.image_id = request.data.get('image')
            vsubcategory.descriptions = request.data.get('descriptions')
            vsubcategory.keywords = request.data.get('keywords')
            vsubcategory.tags = request.data.get('tags')
            vsubcategory.save()
            return Response({'text': 'ok','id' :request.data.get('id') })
        else:
            vsubcategory = subcategory.objects.create(name=request.data.get('name'),category_id=request.data.get('category'),showindexpage=request.data.get('showindexpage'),image_id=request.data.get('image'),descriptions=request.data.get('descriptions'),keywords=request.data.get('keywords'),tags=request.data.get('tags'))
            return Response({'text': 'ok','idv':vsubcategory.id})
    except:
        return Response({'text': 'bad'})
def manage_tree_menu(request):
    form = tree_menu()
    datas = treemenu.objects.all() or False
    content = {
        'title': "مدیریت منو ها",
        'form': form,
        'datas': datas,
    }
    return render(request, "dashboard/treemenu.html", content)
@api_view(['POST'])
def deletetreemenu(request):
    try:
        vtreemenu = treemenu.objects.get(id = request.data.get('id'))
        vtreemenu.delete()
        return Response({'text': 'ok'})
    except:
        return Response({'text': 'bad'})
@api_view(['POST'])
def settreemenu(request):
    try:
        if request.data.get('id'):
            vtreemenu = treemenu.objects.get(id = request.data.get('id'))
            vtreemenu.name= request.data.get('name')
            vtreemenu.tree = request.data.get('tree')
            vtreemenu.link = request.data.get('link')
            vtreemenu.save()
            return Response({'text': 'ok','id' :request.data.get('id') })
        else:
            vtreemenu = treemenu.objects.create(name = request.data.get('name'),tree = request.data.get('tree'),link=request.data.get('link'))
            return Response({'text': 'ok','idv':vtreemenu.id})
    except:
        return Response({'text': 'bad'})
def manage_menu(request):
    form = menu_()
    datas = menu.objects.all() or False
    content = {
        'title': "مدیریت منو ها",
        'form': form,
        'datas': datas,
    }
    return render(request, "dashboard/menu.html", content)
@api_view(['POST'])
def deletemenu(request):
    try:
        vmenu = menu.objects.get(id = request.data.get('id'))
        vmenu.delete()
        return Response({'text': 'ok'})
    except:
        return Response({'text': 'bad'})
@api_view(['POST'])
def setmenu(request):
    try:
        if request.data.get('id'):
            vmenu = menu.objects.get(id = request.data.get('id'))
            vmenu.name= request.data.get('name')
            vmenu.tree_id = request.data.get('tree')
            vmenu.save()
            return Response({'text': 'ok','id' :request.data.get('id') })
        else:
            vmenu = menu.objects.create(name = request.data.get('name'),tree_id = request.data.get('tree'))
            return Response({'text': 'ok','idv':vmenu.id})
    except:
        return Response({'text': 'bad'})
def manage_sub_menu(request ):
    form = sub_menu()
    datas = submenu.objects.all() or False
    content = {
        'title': "مدیریت منو ها",
        'form': form,
        'datas': datas,
    }
    return render(request, "dashboard/submenu.html", content)
@api_view(['POST'])
def deletesubmenu(request):
    try:
        vsubmenu = submenu.objects.get(id = request.data.get('id'))
        vsubmenu.delete()
        return Response({'text': 'ok'})
    except:
        return Response({'text': 'bad'})
@api_view(['POST'])
def setsubmenu(request):
    try:
        if request.data.get('id'):
            vsubmenu = submenu.objects.get(id = request.data.get('id'))
            vsubmenu.selectmenu_id= request.data.get('selectmenu')
            vsubmenu.category_id = request.data.get('category')
            vsubmenu.save()
            return Response({'text': 'ok','id' :request.data.get('id') })
        else:
            vsubmenu = submenu.objects.create(selectmenu_id = request.data.get('selectmenu'),category_id = request.data.get('category'))
            return Response({'text': 'ok','idv':vsubmenu.id})
    except:
        return Response({'text': 'bad'})
def manage_brand(request):
    form = brand_()
    datas = brand.objects.all() or False
    select_images = images.objects.all() or False
    content = {
        'title': "برند ها",
        'form': form,
        'datas': datas,
        'select_images': select_images,
    }
    return render(request, "dashboard/brand.html", content)
@api_view(['POST'])
def deletebrand(request):
    try:
        vbrand = brand.objects.get(id = request.data.get('id'))
        vbrand.delete()
        return Response({'text': 'ok'})
    except:
        return Response({'text': 'bad'})
@api_view(['POST'])
def setbrand(request):
    try:
        if request.data.get('id'):
            vbrand = brand.objects.get(id = request.data.get('id'))
            vbrand.name = request.data.get('name')
            vbrand.showindexpage = request.data.get('showindexpage')
            vbrand.image_id = request.data.get('image')
            vbrand.descriptions = request.data.get('descriptions')
            vbrand.keywords = request.data.get('keywords')
            vbrand.tags = request.data.get('tags')
            vbrand.save()
            return Response({'text': 'ok','id' :request.data.get('id') })
        else:
            vbrand = brand.objects.create(name=request.data.get('name'),showindexpage=request.data.get('showindexpage'),image_id=request.data.get('image'),descriptions=request.data.get('descriptions'),keywords=request.data.get('keywords'),tags=request.data.get('tags'))
            return Response({'text': 'ok','idv':vbrand.id})
    except:
        return Response({'text': 'bad'})
def manage_color(request):
    form = color_()
    datas = color.objects.all() or False
    content = {
        'title': "مدیریت رنگ ها",
        'form': form,
        'datas': datas,
    }
    return render(request, "dashboard/color.html", content)
@api_view(['POST'])
def deletecolor(request):
    try:
        vcolor = color.objects.get(id = request.data.get('id'))
        vcolor.delete()
        return Response({'text': 'ok'})
    except:
        return Response({'text': 'bad'})
@api_view(['POST'])
def setcolor(request):
    try:
        if request.data.get('id'):
            vcolor = color.objects.get(id = request.data.get('id'))
            vcolor.color = request.data.get('color')
            vcolor.name = request.data.get('name')
            vcolor.save()
            return Response({'text': 'ok','id' :request.data.get('id') })
        else:
            vcolor = color.objects.create(name=request.data.get('name'),color=request.data.get('color'))
            return Response({'text': 'ok','idv':vcolor.id})
    except:
        return Response({'text': 'bad'})
def manage_warranty(request):
    form = warranty_()
    datas = warranty.objects.all() or False
    content = {
        'title': "مدیریت گارانتی ها",
        'form': form,
        'datas': datas,
    }
    return render(request, "dashboard/warranty.html", content)
@api_view(['POST'])
def deletewarranty(request):
    try:
        vwarranty = warranty.objects.get(id = request.data.get('id'))
        vwarranty.delete()
        return Response({'text': 'ok'})
    except:
        return Response({'text': 'bad'})
@api_view(['POST'])
def setwarranty(request):
    try:
        if request.data.get('id'):
            vwarranty = warranty.objects.get(id = request.data.get('id'))
            vwarranty.name = request.data.get('name')
            vwarranty.save()
            return Response({'text': 'ok','id' :request.data.get('id') })
        else:
            vwarranty = warranty.objects.create(name=request.data.get('name'))
            return Response({'text': 'ok','idv':vwarranty.id})
    except:
        return Response({'text': 'bad'})
def manage_details(request):
    form = details_()
    datas = details.objects.all() or False
    content = {
        'title': "مدیریت خصوصیات ",
        'form': form,
        'datas': datas,
    }
    return render(request, "dashboard/details.html", content)
@api_view(['POST'])
def deletedetails(request):
    try:
        vdetails = details.objects.get(id = request.data.get('id'))
        vdetails.delete()
        return Response({'text': 'ok'})
    except:
        return Response({'text': 'bad'})
@api_view(['POST'])
def setdetails(request):
    try:
        if request.data.get('id'):
            vdetails = details.objects.get(id = request.data.get('id'))
            vdetails.name = request.data.get('name')
            vdetails.save()
            return Response({'text': 'ok','id' :request.data.get('id') })
        else:
            vdetails = details.objects.create(name=request.data.get('name'))
            return Response({'text': 'ok','idv':vdetails.id})
    except:
        return Response({'text': 'bad'})
def manage_value_details(request):
    form = value_details_()
    datas = valuedetails.objects.all() or False
    content = {
        'title': "مدیریت خصوصیات ",
        'form': form,
        'datas': datas,
    }
    return render(request, "dashboard/valuedetails.html", content)
@api_view(['POST'])
def deletevaluedetails(request):
    try:
        vvaluedetails = valuedetails.objects.get(id = request.data.get('id'))
        vvaluedetails.delete()
        return Response({'text': 'ok'})
    except:
        return Response({'text': 'bad'})
@api_view(['POST'])
def setvaluedetails(request):
    try:
        if request.data.get('id'):
            vvaluedetails = valuedetails.objects.get(id = request.data.get('id'))
            vvaluedetails.value = request.data.get('name')
            vvaluedetails.namedetails_id = request.data.get('parent')
            vvaluedetails.save()
            return Response({'text': 'ok','id' :request.data.get('id'),'parentname' : vvaluedetails.namedetails.name})
        else:
            vvaluedetails = valuedetails.objects.create(value=request.data.get('name'),namedetails_id=request.data.get('parent'))
            return Response({'text': 'ok','idv':vvaluedetails.id,'parentname' : vvaluedetails.namedetails.name})
    except:
        return Response({'text': 'bad'})
def variable_(request):
    form = Variable_()
    datas = Variable.objects.all() or False
    content = {
        'datas' : datas,
        'title': "مدیریت متغیر ها ",
        'form' : form,
    }
    return render(request, 'dashboard/variable.html' , content)
@api_view(['POST'])
def deletevariable(request):
    try:
        vVariable = Variable.objects.get(id = request.data.get('id'))
        vVariable.delete()
        return Response({'text': 'ok'})
    except:
        return Response({'text': 'bad'})
@api_view(['POST'])
def setvariable(request):
    try:
        if request.data.get('id'):
            vVariable = Variable.objects.get(id = request.data.get('id'))
            vVariable.name = request.data.get('name')
            vVariable.save()
            return Response({'text': 'ok','id' :request.data.get('id')})
        else:
            vVariable = Variable.objects.create(name=request.data.get('name'))
            return Response({'text': 'ok','idv':vVariable.id})
    except:
        return Response({'text': 'bad'})
def create_product(request):
    if request.method == "POST":
        form = product_(request.POST )
        if form.is_valid():
            form.save()
            return redirect('show_products')
        else:
            datas = valuedetails.objects.all()
            content = {
                'form': form,
                'datas': datas,
            }
            return render(request, 'dashboard/create_product.html', content)
    datas = valuedetails.objects.all()
    form = product_()
    content = {
        'form' : form,
        'datas' : datas,
    }
    return render(request, 'dashboard/create_product.html' , content)
def del_product(request):
    pro = request.GET.get('product')
    id = get_object_or_404(product , pk= pro)
    id.delete()
    return HttpResponseRedirect('show_products')
def update_product(request):
    if request.method == "POST":
        pro = request.GET.get('product')
        id = get_object_or_404(product, pk=pro)
        form = product_(request.POST, instance=id)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('show_products')
        else:
            datas = valuedetails.objects.all()
            content = {
                'form': form,
                'datas': datas,
                'id': id,
            }
            return render(request, 'dashboard/update_product.html', content)
    pro = request.GET.get('product')
    id = get_object_or_404(product, pk=pro)
    form = product_(instance=id)
    datas = valuedetails.objects.all()
    content = {
        'form': form,
        'datas': datas,
        'id': id,
    }
    return render(request, 'dashboard/update_product.html', content)
def show_products(request):
    datas = product.objects.all() or False
    content = {
        'title': "نمایش محصولات",
        'datas': datas,
    }
    return render(request, "dashboard/show_products.html", content)
def set_price(request , product_id):
    if request.method == "POST":
        form = Variable_price_(request.POST)
        if form.is_valid():
            form.save()
        else:

            try:
                datas = Variable_price.objects.filter(product_id=product_id)
            except:
                datas = False
            try:
                pro = product.objects.get(id=product_id)
            except:
                pro = False
            form = Variable_price_()
            colors = color.objects.all() or False
            content = {
                'title': "ثبت قیمت محصولات",
                'datas': datas,
                'form': form,
                'pro': pro,
                'colors': colors,
                'product_id': product_id,
            }
            return render(request, "dashboard/set_price.html", content)
    try:
        datas = Variable_price.objects.filter(product_id = product_id)
    except:
        datas = False
    try:
        pro = product.objects.get(id = product_id)
    except:
        pro = False
    form = Variable_price_()
    colors = color.objects.all() or False
    content = {
        'title': "ثبت قیمت محصولات",
        'datas': datas,
        'form': form,
        'pro': pro,
        'colors' : colors,
        'product_id' : product_id,
    }
    return render(request, "dashboard/set_price.html", content)
def update_price(request):
    ins = Variable_price.objects.get(id = request.POST.get('id'))
    form = Variable_price_(request.POST, instance=ins)
    if form.is_valid():
        form.save()
    return redirect(request.POST.get('url'))
def del_price(request):
    ins = Variable_price.objects.get(id = request.POST.get('id'))
    ins.delete()
    return redirect(request.POST.get('url'))
def list_price(request):
    datas = product.objects.all() or False
    step = request.GET.get('step', 10)
    result = False
    if datas:
        paginator = Paginator(datas, step)
        page = request.GET.get('page', 1)
        try:
            result = paginator.page(page)
        except PageNotAnInteger:
            result = paginator.page(1)
        except EmptyPage:
            result = paginator.page(paginator.num_pages)
    content = {
        'title': "محصولات محصولات",
        'datas': result,
    }
    return render(request, "dashboard/listprice.html", content)
def product__(request,proid,proname):
    product_select = get_object_or_404(product,id = proid)
    if product_select.visibility == False:
        return redirect('e404')
    other_product = product.objects.filter(category=product_select.category.first().id) or False
    pro_price = Variable_price.objects.filter(product_id = proid) or False
    [x.checkdate() for x in pro_price]
    comment = comment_product.objects.filter(product_id = proid , show=True) or False
    form = product_comment_()
    valtreemenu = treemenu.objects.all() or False
    valmenu = menu.objects.all() or False
    valsubmenu = submenu.objects.all() or False
    star_avg = int(statistics.mean(map(lambda x : x.starts, comment))) if comment else  False
    product_select.pro_view()
    valsub_footer = sub_footer.objects.all() or False
    valmain_footer = main_footer.objects.all() or False
    logo = logo_site.objects.all() or False
    content = {
        'valtreemenu': valtreemenu,
        'valmenu': valmenu,
        'valsubmenu': valsubmenu,
        'product_select': product_select,
        'pro_price': pro_price,
        'comment': comment,
        'form': form,
        'star_avg': star_avg,
        'other_product': other_product,
        'valsub_footer': valsub_footer,
        'valmain_footer': valmain_footer,
        'logo': logo,
    }
    return render(request, "main/product.html", content)
@api_view(['POST'])
def product_comment(request):
    try:
        datas = request.data
        ts = str(int(datetime.timestamp(datetime.now())))
        comment = comment_product.objects.create(product_id=datas.get('product_id'),account_id=request.user.id,title=datas.get('title'),starts=datas.get('stars'),text=datas.get('text'),sendtime=ts)
        comment.save()
        text = 'ok'
    except:
         text = 'bad'
    return Response({'text':text})
def check_comment_product(request):
    comment = reversed(comment_product.objects.all()) or False
    content = {
        'title' : 'نظرات',
        'datas' : comment,
    }
    return render(request , 'dashboard/allow_comment.html' , content)
@api_view(['GET'])
def get_data_comment(request):
    comment_id = request.GET.get('data', None)
    comment = comment_product.objects.get(id = comment_id) or False

    return Response({
        'text' : comment.text,
    })
@api_view(['POST'])
def change_show_comment(request):
    comment_id = request.data.get('comment_id', None)
    comment = comment_product.objects.get(id = comment_id) or False
    status = None
    if comment.show:
        comment.show = False
        comment.save()
        status = "ok"
    else:
        comment.show = True
        comment.save()
        status = "ok"
    return Response({
        'status': status,
    })
def checkcart(request , datas):
    carts = request.session['cart']
    prices = Variable_price.objects.get(id=datas[0])
    status = "bad"

    request.session['cart'] = carts
    return status
@api_view(['POST'])
def add_to_cart(request):
    status = "bad"
    price_id = int(request.data.get('product_id'))
    pri = Variable_price.objects.get(id = price_id)
    dcount = int(request.data.get('count'))
    try:
        data = cart.objects.get(user_id=int(request.user.id), pri_id=price_id)
    except:
        data = False
    if data:
        if request.user.colleague:
            if pri.max_colleague  >= (dcount + data.count) and pri.count >= (dcount+data.count):
                data.count += dcount
                status = "ok"
                print(1)
        else:
            if pri.max >= (dcount + data.count) and pri.count >= (dcount + data.count):
                data.count += dcount
                status = "ok"
                print(2)
    else:
        data = cart.objects.create(user = request.user ,pri = pri,pro = pri.product,count = dcount)
        status = "ok"
        print(3)
    print(data.count)
    data.save()
    print(data.count)
    return Response({
        'status': status,
    })
@api_view(['POST'])
def low_to_cart(request):
    status = "bad"
    try:
        data = cart.objects.get(user_id=int(request.user.id), pri_id=int(request.data.get('product_id')))
        data.count -= 1
        data.save()
        status = "ok"
    except:
        data = False
    return Response({
        'status': status,
    })
@api_view(['POST'])
def remove_to_cart(request):
    status = "bad"
    try:
        data = cart.objects.get(user_id=int(request.user.id), pri_id=int(request.data.get('product_id')))
        data.delete()
        status = "ok"
    except:
        data = False
    return Response({
        'status': status,
    })
@api_view(['GET'])
def get_data_cart(request):
    data = cart.objects.filter(user=request.user)
    pl = []
    [pl.append(x.pro.return_cart(x.pri.show_price(request),x.count,x.id)) for x in data]
    price = sum([x['price'] * x['count'] for x in pl])
    return Response({
        'text' : pl,
        'price' : price,
    })
def product_grid(request):
    try:
        filter = request.GET.get('filter', False)
        if filter:
            set_filter = '{%s}' % filter
            set_filter = json.loads(set_filter)
            pro = product.objects.filter(**set_filter) or False
        else:
            pro = product.objects.all() or False
        result = False
        brands = [x.brand for x in pro]
        brands = list(set(brands))
        categories = [x.category.first() for x in pro]
        categories = list(set(categories))
        valbrand = brand.objects.all()
        if pro:
            paginator = Paginator(pro, 18)
            page = request.GET.get('page', 1)
            try:
                result = paginator.page(page)
            except PageNotAnInteger:
                result = paginator.page(1)
            except EmptyPage:
                result = paginator.page(paginator.num_pages)
        logo = logo_site.objects.all() or False
        content = {
            'title': 'همه محصولات',
            'products': result,
            'logo': logo,
            'brands': brands,
            'categories': categories,
            'valbrand': valbrand,
        }
        return render(request, "main/products-grid.html", content)
    except:
        return render(request, 'main/page-error-404.html')

def e404(request):
    valtreemenu = treemenu.objects.all() or False
    valmenu = menu.objects.all() or False
    valsubmenu = submenu.objects.all() or False
    pro = product.objects.filter(category=1)
    content = {
        'valtreemenu': valtreemenu,
        'valmenu': valmenu,
        'valsubmenu': valsubmenu
    }
    return render(request,"main/page-error-404.html", content)