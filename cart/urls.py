from django.urls import path
from .views import cart_view, add_to_cart, remove_from_cart, CartByUserView

app_name = 'cart'

urlpatterns = [
    path('', cart_view, name='cart_url'),
    path('add/', add_to_cart, name='add_to_cart_url'),
    path('remove/', remove_from_cart, name='remove_from_cart_url'),
    path('<int:cart_id>/', CartByUserView.as_view(), name='cart_by_user_url'),
]
