from django.urls import path
from . import views

urlpatterns = [
    path('getuserpaymentdetails/', views.getUserPaymentDetails),
    path('adduserpaymentdetails/', views.addUserPaymentDetails),
    path('updateuserpaymentdetails/<pk>', views.updateUserPaymentDetaild),
    path('deleteuserpaymentdetails/<pk>', views.deleteUserPaymentDetails),
]
