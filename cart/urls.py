from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/remove', views.remove, name="remove"),
    path('<int:id>/add', views.add, name="add"),
    path('view/', views.view, name="cartView"),
]