from django.urls import path
from . import views

app_name = 'cart'  # ← This line is important!

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),           # ← This line
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]