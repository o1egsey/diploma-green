from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from basket.basket import Basket
from orders.models import Order, OrderItem


@login_required
def checkout(request):
    """

    :param request:
    :return:
    """
    basket = Basket(request)
    return render(request, 'checkout/checkout.html', {'basket': basket})


@login_required
def placeorder(request):
    """

    :param request:
    :return:
    """
    basket = Basket(request)
    if request.method == 'POST':
        neworder = Order()
        neworder.user = request.user
        neworder.first_name = request.POST.get('fname')
        neworder.surname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.city = request.POST.get('city')
        neworder.warehouse = request.POST.get('warehouse')
        neworder.payment_option = request.POST.get('payment_option')
        total_paid = basket.get_subtotal_price()
        neworder.total_paid = total_paid
        neworder.billing_status = True
        neworder.save()
        order_id = neworder.pk

        for item in basket:
            OrderItem.objects.create(order_id=order_id,
                                     product=item["product"],
                                     price=item["price"],
                                     quantity=item["qty"])

        basket.clear_session()

        messages.success(request, "Замовлення успішне, перейдіть в Кабінет, щоб переглянути деталі")

    return redirect('/')

# def basket_delete(request):
#     basket = Basket(request)
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('productid'))
#         basket.delete(product=product_id)
#
#         basketqty = basket.__len__()
#         baskettotal = basket.get_subtotal_price()
#         response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
#         return response
#
#
# def basket_update(request):
#     basket = Basket(request)
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('productid'))
#         product_qty = int(request.POST.get('productqty'))
#         basket.update(product=product_id, qty=product_qty)
#
#         basketqty = basket.__len__()
#         baskettotal = basket.get_subtotal_price()
#         response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
#         return response

