from django.urls import path
from . import views

# This is a list of all the urls that the API will respond to.
urlpatterns = [
    path('getuserorder/', views.getUserOrder),
    path('adduserorder/', views.userOrdering),
]
