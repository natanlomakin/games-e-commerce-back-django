from django.urls import path
from . import views

urlpatterns = [
    path('getuserprofile/', views.getUserProfile),
    path('adduserprofile/', views.addUserProfile),
    path('deleteuserprofile/<pk>', views.deleteUserProfile),
    path('updateuserprofile/<pk>', views.updateUserProfile),
]
