from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('about/', views.about),
    path('concerts/', views.concerts),
    path('contact/', views.contact),
    path('gallery/', views.gallery),
    path('login/', views.login),
    path('signup/', views.signup),
    path('usertable/', views.usertable),
    path('addBand/', views.addBand),
    path('cards/', views.cards),
    path('cart/', views.cart),
    path('email/', views.email),
    path('remove_from_cart/<int:pk>', views.remove_from_cart, name='remove_from_cart'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('addTOcart/<int:pk>', views.addTOcart, name='cart'),

]