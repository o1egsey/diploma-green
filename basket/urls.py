from django.urls import path
from . import views

app_name = 'basket'
urlpatterns = [
    path('', views.showBasketSummary, name='basket_summary'),
    path('add/', views.addToBasket, name='basket_add'),
    path('delete/', views.deleteItemFromBasket, name='basket_delete'),
    path('update/', views.editBasket, name='basket_update'),
]
