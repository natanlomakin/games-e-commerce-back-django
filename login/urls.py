from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


# This is the url for the login and refresh token.
urlpatterns = [
    path('loginuser/', views.MyTokenObtainPairView.as_view()),
    path('refreshaccess/', TokenRefreshView.as_view(), name='token_refresh'),
]
