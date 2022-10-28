from django.urls import path
from . import views

urlpatterns = [
    path('getuserorder/', views.getUserOrder),
    path('adduserorder/', views.userOrdering),
]
