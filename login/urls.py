from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('loginuser/', views.MyTokenObtainPairView.as_view()),
    path('refreshaccess/', TokenRefreshView.as_view(), name='token_refresh'),
]
