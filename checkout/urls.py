from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    #path('process/', views.process_order, name='process_order'),
    path('process-paypal/', views.process_paypal_payment, name='process_paypal_payment'),
]