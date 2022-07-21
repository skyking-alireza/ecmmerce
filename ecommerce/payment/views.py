import uuid

from django.db import connection
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from idpay.api import IDPayAPI

from account.models import payment, cart, customers


def payment_init():
    return IDPayAPI('6a7f99eb-7c20-4412-a972-6dfb7cd253a4', 'http://127.0.0.1', True)
@csrf_exempt
def payment_start(request):
    if request.method == "POST":
        order_id = uuid.uuid1()
        ins = get_object_or_404(customers, id=request.user.id)
        carts = cart.objects.filter(user=request.user or False)
        pl = []
        [pl.append(x.pro.return_cart(x.pri.show_price(request), x.count, x.pri_id)) for x in carts]
        price = sum([x['price'] * x['count'] for x in pl])
        payer = {
            'name': ins.get_full_name(),
            'phone': ins.phone_number,
            'mail': ins.email,
            'desc': 'test',
        }
        record = payment(order_id=order_id, amount=price , status=2 , user_id=ins.id ,payment_id='****' , user_address_id=int(request.POST.get('address')))
        record.save()
        idpay_payment = payment_init()
        result = idpay_payment.payment(str(order_id), price, '/payment/payment_return', payer)

        if 'id' in result:
            record.status = 1
            record.payment_id = result['id']
            record.save()

            return redirect(result['link'])

        else:
            txt = result['message']
    else:
        return  redirect('index')
@csrf_exempt
def payment_return(request):
    if request.method == 'POST':

        pid = request.POST.get('id')
        status = request.POST.get('status')
        pidtrack = request.POST.get('track_id')
        order_id = request.POST.get('order_id')
        amount = request.POST.get('amount')
        card = request.POST.get('card_no')
        date = request.POST.get('date')

        if payment.objects.filter(order_id=order_id, payment_id=pid, amount=amount, status=1).count() == 1:
            idpay_payment = payment_init()
            paymentt = payment.objects.get(payment_id=pid, amount=amount)
            paymentt.status = status
            paymentt.date = str(date)
            paymentt.card_number = card
            paymentt.idpay_track_id = pidtrack
            paymentt.save()
            queryrun = connection.cursor()
            queryrun.execute('INSERT INTO account_orders (pro_id,count, price_id,payment_id_id,user_id) SELECT pro_id,count, pri_id , {} , {} FROM account_cart WHERE user_id = {}'.format(str(paymentt.id),paymentt.user_id,paymentt.user_id))
            queryrun.execute('DELETE FROM account_cart WHERE user_id = {}'.format(paymentt.user_id))

            if status == '10':
                result = idpay_payment.verify(pid, paymentt.order_id)
                if 'status' in result:
                    paymentt.status = result['status']
                    paymentt.bank_track_id = result['payment']['track_id']
                    paymentt.save()
                    css = 'success'

                    content = {
                        'txt': 'تراکنش موفقیت امیز بود',
                        'css' : css,
                    }
                    return render(request, 'main/page-after-payment.html', content)
                else:
                    css = 'danger'
                    txt = result['message']
            else:
                css = 'primary'
                txt = "کد خطا : " + str(status) + "   |   " + "توضیخات : " + idpay_payment.get_status(status)
        else:
            css = 'warning'
            txt = "خرید پیدا نشد"
    else:
        css = 'danger'
        txt = "درخواست شما رد شد"
    return render(request, 'main/page-after-payment.html', {'txt': txt,'css' : css})