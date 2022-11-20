from django.urls import path
from . import views

# This is a list of all the urls that the API will respond to.
urlpatterns = [
    path('getuserpaymentdetails/', views.getUserPaymentDetails),
    path('adduserpaymentdetails/', views.addUserPaymentDetails),
    path('updateuserpaymentdetails/<pk>', views.updateUserPaymentDetaild),
    path('deleteuserpaymentdetails/<pk>', views.deleteUserPaymentDetails),
]
