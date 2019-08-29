from django.urls import path
from . import views
app_name= 'app_asj'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('market/', views.market, name='market'),
    path('cart/', views.cart, name='cart'),
    path('mine/', views.mine, name='mine'),
    path('base/', views.base, name='base')
]