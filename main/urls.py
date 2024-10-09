from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_to_cart/<int:game_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('remove_from_cart/<int:game_id>/', views.remove_from_cart, name='remove_from_cart'),
]
