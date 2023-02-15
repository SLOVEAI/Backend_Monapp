from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.user_detail_view),
    path('<int:pk>/update/', views.user_udpate_view),
    path('', views.user_create_view),
]