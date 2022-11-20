from django.urls import path
from . import views

# This is a list of all the urls that the API will respond to.
urlpatterns = [
    path('getuserprofile/', views.getUserProfile),
    path('adduserprofile/', views.addUserProfile),
    path('deleteuserprofile/<pk>', views.deleteUserProfile),
    path('updateuserprofile/<pk>', views.updateUserProfile),
]
