from django.urls import path

from . import views

urlpatterns = [
    path('hoodies/', views.hoodie_index, name="hoodie-index"),
]
