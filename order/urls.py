from django.urls import path
from . import views

# This is a list of all the urls that the API will respond to.
urlpatterns = [
    path('getuserorder/', views.getUserOrders),
    path('singleorder/<pk>', views.getUserSingleOrder),
    path('adduserorder/', views.userOrdering),
]
