from django.urls import path, include
from . import views

urlpatterns = [
    path('catalog/', views.index, name="main"),
    path('catalog/<int:id>/view', views.book, name="view"),
    path('catalog/<int:id>/buy', views.buy, name="buy"),
]
