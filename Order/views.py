from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Order.models import Order, OrderDetail

# Create your views here.
from Product.models import Product


@login_required(login_url="login_account")
def add_user_order(request):
    context = {}
    if request.method == "POST":
        product_id = request.POST.get("product_id_input")
        product = Product.objects.get(id=product_id)
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)

        OrderDetail.objects.create(order_id=order.id, product_id=product.id, price=product.price, count=1)

    return redirect('Order:card_page')


@login_required(login_url="login_account")
def card_page(request):
    open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    context = {}
    if open_order is not None:
        context["order"] = open_order
        context["detail"] = open_order.orderdetail_set.all()
    return render(request, 'Order/card.html', context)
