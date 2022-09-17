from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('getuserpaymentdetails/', views.getUserPaymentDetails),
    path('adduserpaymentdetails/', views.addUserPaymentDetails),
    path('updateuserpaymentdetails/<pk>', views.updateUserPaymentDetaild),
    path('deleteuserpaymentdetails/<pk>', views.deleteUserPaymentDetails),
]
