from django.urls import path
from . import views
from .views import signup, login, logout
from .views import vensg, venlt, venlo

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('packages/', views.packages, name='packages'),
    path('products/', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('product/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('vensg/', vensg, name='vensg'),
    path('venlo/', venlo, name='venlo'),
    path('venlt/', venlt, name='venlt'),
    path('product/<int:product_id>/pay/', views.create_order, name='create_order'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('munnar/',views.munnar,name='munnar'),
    path('aleppy/',views.aleppy,name='aleppy'),
    path('wayanad/',views.wayanad,name='wayanad'),
    path('cochin/',views.cochin,name='cochin'),
    
    
    
]
