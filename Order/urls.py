from django.urls import path
from Order.views import add_user_order, card_page

app_name = "Order"
urlpatterns = [
    path('order-card', add_user_order, name="order_card"),
    path('card', card_page, name="card_page"),
]
