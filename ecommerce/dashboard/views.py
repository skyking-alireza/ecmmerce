from datetime import datetime, timedelta, timezone

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from rest_framework.decorators import api_view
from rest_framework.response import Response
import gallery.models
from account.models import payment, orders, customers
from account.serializers import return_data_payment
from main.models import *
from product.models import product, comment_product
from .forms import _page_generate_, _main_footer, _sub_footer, _navbar_process, _swiper, _blog_, _blog_Category
from .models import *
from .serializers import return_data_logo


def generator_page(request):
   if request.method == "POST":
      req = request.POST.copy()
      req['url'] = slugify(req['title'], allow_unicode=True)
      if request.POST.get('page-id') :
         ins = page_generator.objects.get(id =request.POST.get('page-id')) or False
         form  = _page_generate_(req, instance=ins)
      else:
         form = _page_generate_(req)
      if form.is_valid():
         form.save()
         return  redirect('generator_page')
      else:
         select_images = gallery.models.images.objects.all() or False
         datas = page_generator.objects.all() or False
         content = {
            'form': form,
            'select_images': select_images,
            'datas': datas,
         }
         return render(request, 'dashboard/page_generator.html', content)
   form  = _page_generate_()
   select_images = gallery.models.images.objects.all() or False
   datas = page_generator.objects.all() or False
   content = {
      'form' : form,
      'select_images' : select_images,
      'datas': datas,
   }
   return render(request, 'dashboard/page_generator.html' , content)
def delete_page(request , page_id):
   data = page_generator.objects.get(pk = page_id)
   data.delete()
   return redirect('generator_page')
@api_view(['GET'])
def update_page(request):
   page_id = request.GET.get('data', None)
   page = page_generator.objects.get(id=page_id) or False
   if page:
      page = {'id' : page.id ,'url' : page.url ,'title' : page.title ,'description_seo' : page.description_seo ,'keywords_seo' : page.keywords_seo,'tags_seo' : page.tags_seo,'image' : page.image.id,'text' : page.text }
   return Response({
      'text': page,
   })
def main_footer_(request):
   if request.method == "POST":
      if request.POST.get('footer-id') :
         ins = main_footer.objects.get(id =request.POST.get('footer-id')) or False
         form = _main_footer(request.POST , instance= ins)
      else:
         form = _main_footer(request.POST)
      if form.is_valid():
         form.save()
         return redirect('main_footer')
      else:
         data = main_footer.objects.all() or False
         content = {
            'form': form,
            'datas': data,
            'title': 'عناوین فوتر',
         }
         return render(request, 'dashboard/footer_main.html', content)
   form = _main_footer()
   data = main_footer.objects.all() or False
   content = {
      'form' : form,
      'datas' : data,
      'title': 'عناوین فوتر',
   }
   return render(request , 'dashboard/footer_main.html' , content)
def delete_footer(request,id_footer):
   data = main_footer.objects.get(pk=id_footer)
   data.delete()
   return redirect('main_footer')
@api_view(['GET'])
def update_footer(request):
   footer_id = request.GET.get('data', None)
   footer = main_footer.objects.get(id=footer_id) or False
   if footer:
      footer = {'id' : footer.id ,'title' : footer.title}
   return Response({
      'text': footer,
   })
def sub_footer_(request):
   data = sub_footer.objects.all() or False
   if request.method == "POST":
      if request.POST.get('footer-id') :
         ins = sub_footer.objects.get(id =request.POST.get('footer-id')) or False
         form = _sub_footer(request.POST , instance= ins)
      else:
         form = _sub_footer(request.POST)
      if form.is_valid():
         form.save()
         return redirect('sub_footer')
      else:
         content = {
            'form': form,
            'datas': data,
            'title': 'زیر مجموعه های فوتر',
         }
         return render(request, 'dashboard/sub_footer.html', content)
   form = _sub_footer()
   content = {
      'form' : form,
      'datas' : data,
      'title': 'زیر مجموعه های فوتر',
   }
   return render(request , 'dashboard/sub_footer.html' , content)
def delete_sub_footer(request,id_sub_footer):
   data = sub_footer.objects.get(pk=id_sub_footer)
   data.delete()
   return redirect('sub_footer')
@api_view(['GET'])
def update_sub_footer(request):
   sub_footer_id = request.GET.get('data', None)
   footer = sub_footer.objects.get(id=sub_footer_id) or False
   if footer:
      footer = {'id' : footer.id ,'title' : footer.title ,'link' : footer.link ,'main' : footer.main.id}
   return Response({
      'text': footer,
   })
def manage_navbar_process(request):
   navbar = navbar_process.objects.all() or False
   select_images = images.objects.all() or False
   if request.method == "POST":
      if request.POST.get('navbar_id'):
         ins = navbar_process.objects.get(id = request.POST.get('navbar_id'))
         form = _navbar_process(request.POST , instance=ins)
      else:
         form = _navbar_process(request.POST)
      if form.is_valid():
         form.save()
         return redirect('navbar_process')
      else:
         content = {
            'title': 'نوار عملکرد',
            'data': navbar,
            'select_images': select_images,
            'form': form,
         }
         return render(request, 'dashboard/navbar_process.html', content)
   form = _navbar_process()
   content = {
      'title' : 'نوار عملکرد',
      'datas' : navbar,
      'select_images' : select_images,
      'form' : form,
   }
   return render(request, 'dashboard/navbar_process.html' , content)
def delete_navbar_process(request,navbar_id):
   ins = navbar_process.objects.get(id = navbar_id)
   ins.delete()
   return redirect('navbar_process')
@api_view(['GET'])
def update_navbar_process(request):
   ins = get_object_or_404(navbar_process ,id = request.GET.get('data') )
   text = {'id' : ins.id , 'title' : ins.title, 'image' : ins.image.id , 'descriptions' : ins.descriptions}
   return Response({
      'text': text,
   })
def manage_swiper(request):
   valswiper = swiper.objects.all() or False
   select_images = images.objects.all() or False
   if request.method == "POST":
      if request.POST.get('swiper_id'):
         ins = swiper.objects.get(id = request.POST.get('swiper_id'))
         form = _swiper(request.POST , instance=ins)
      else:
         form = _swiper(request.POST)
      if form.is_valid():
         form.save()
         return redirect('swiper')
      else:
         content = {
            'title': 'اسلایدر',
            'datas': valswiper,
            'select_images': select_images,
            'form': form,
         }
         return render(request, 'dashboard/swiper.html', content)
   form = _swiper()
   content = {
      'title': 'اسلایدر',
      'datas': valswiper,
      'select_images': select_images,
      'form': form,
   }
   return render(request, 'dashboard/swiper.html' , content)
def delete_swiper(request,swiper_id):
   ins = get_object_or_404(swiper ,id = swiper_id)
   ins.delete()
   return redirect('swiper')
@api_view(['GET'])
def update_swiper(request):
   ins = get_object_or_404(swiper ,id = request.GET.get('data') )
   text = {'id' : ins.id , 'title' : ins.title, 'image' : ins.image.id , 'descriptions' : ins.descriptions, 'link' : ins.link}
   return Response({
      'text': text,
   })
def blog_manager(request):
   valblog = blogs.objects.all()
   select_images = images.objects.all()
   if request.method == "POST":
      req = request.POST.copy()
      req['url'] = slugify(req['title'], allow_unicode=True)
      if request.POST.get('blog-id'):
         ins = blogs.objects.get(id=request.POST.get('blog-id')) or False
         form = _blog_(req, instance=ins)
      else:
         form = _blog_(req)
      if form.is_valid():
         form.save()
         return redirect('blogs')
      else:
         select_images = gallery.models.images.objects.all() or False
         datas = blogs.objects.all() or False
         content = {
            'form': form,
            'title': 'وبلاگ',
            'select_images': select_images,
            'datas': datas,
         }
         return render(request, 'dashboard/blogs.html', content)
   form = _blog_()
   content = {
      'form' : form,
      'title' : 'وبلاگ',
      'datas' : valblog,
      'select_images' : select_images,
   }
   return render(request, 'dashboard/blogs.html' , content)
def delete_blogs(request, blogs_id):
   ins = get_object_or_404(blogs , id = blogs_id)
   ins.delete()
   return redirect('blogs')
@api_view(['GET'])
def update_blogs(request):
   ins = get_object_or_404(blogs, id=request.GET.get('data'))
   text = {'id': ins.id, 'title': ins.title,'url': ins.url,'category': ins.category_id,'description_seo': ins.description_seo,'keywords_seo': ins.keywords_seo,'tags_seo': ins.tags_seo, 'image': ins.image.id, 'text': ins.text}
   return Response({
      'text': text,
   })
def category_blog_manager(request):
   datas = category_blog.objects.all()
   if request.method == "POST":
      if request.POST.get('categoryblog-id'):
         ins = category_blog.objects.get(id=request.POST.get('categoryblog-id')) or False
         form = _blog_Category(request.POST, instance=ins)
      else:
         form = _blog_Category(request.POST)
      if form.is_valid():
         form.save()
         return redirect('category_blog')
      else:
         datas = category_blog.objects.all() or False
         content = {
            'form': form,
            'title': 'دسته بندی بلاگ',
            'datas': datas,
         }
         return render(request, 'dashboard/category_blog.html', content)
   form = _blog_Category()
   content = {
      'form' : form,
      'title' : 'دسته بندی بلاگ',
      'datas' : datas,
   }
   return render(request, 'dashboard/category_blog.html', content)
def category_delete_blogs(request, catblogs_id):
   ins = get_object_or_404(category_blog , id = catblogs_id)
   ins.delete()
   return redirect('category_blog')
@api_view(['GET'])
def category_update_blogs(request):
   ins = get_object_or_404(category_blog, id=request.GET.get('data'))
   text = {'id': ins.id, 'title': ins.title}
   return Response({
      'text': text,
   })

def payments_view(request):
   pays = payment.objects.filter(status=100)
   content = {
      'datas' : pays,
      'title' : 'تراکنش ها'
   }
   return render(request, 'dashboard/orders.html' ,content )
@api_view(['POST'])
def change_payment_status(request):
   status_id = request.data.get('status_id')
   pays = payment.objects.filter(status=status_id or False)
   if pays:
      datas = return_data_payment(pays,many=True)
      return Response(datas.data)
   else:
      return Response({'data' : 'not found'})
def view_order_details(request,uuid):
   data = get_object_or_404(payment,order_id=uuid)
   orders_data = orders.objects.filter(payment_id=data.id)
   content = {
      'title' : 'مخشصات سفارش',
      'data' :data,
      'orders_data' :orders_data,
   }
   return render(request, 'dashboard/orders-details.html',content)
@api_view(['GET'])
def dashbord_header(request):
   logo = logo_site.objects.first() or False
   log = return_data_logo(logo,many=False)
   return Response(log.data)
def dashboard(request):
   countuser = customers.objects.count()
   countpayment = payment.objects.all()
   sumamount = sum([int(x.amount) for x in payment.objects.filter(status__lt=100)])
   vs = viewsite.objects.get(id=1)
   today = datetime.now()
   start = (today - timedelta(days=today.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
   timestamp = start.replace(tzinfo=timezone.utc).timestamp()
   countorders = orders.objects.order_by('-id')[:5]
   countpro = product.objects.all().order_by('countview')[:5]
   countcommentpro = comment_product.objects.order_by('-id')[:10]
   content = {
      'countuser' : countuser,
      'countpayment' : countpayment,
      'sumamount' : sumamount,
      'viewsite' : vs,
      'timestamp' : timestamp,
      'title' : 'داشبورد',
      'countorders' : countorders,
      'countpro' : countpro,
      'countcommentpro' : countcommentpro,
   }
   return render(request, 'dashboard/dashboard.html',content)