from django.urls import path

from . import views
from user.views import ListApiView
from user.views import RetrieveUserApiView
from user.views import LoginApiView
from user.views import CreateUserApiView



urlpatterns = [
    path('check', views.api_home),
    path('allusers', views.all_user),
    path('auth/user/all/', ListApiView.as_view()),
    path('auth/user/<pk>/', RetrieveUserApiView.as_view()),
    path('auth/login/', LoginApiView),
    path('auth/signup/', CreateUserApiView.as_view()),
]
