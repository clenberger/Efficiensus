from django.urls import path

from . import views

urlpatterns = [
    path('hoodies/', views.hoodie_index, name="hoodies-index"),
    path('hoodies/', views.PageListView, name="hoodies-list")
]
