from django.urls import path
from . import views

urlpatterns = [
     path('loginuser/', views.MyTokenObtainPairView.as_view()),
]