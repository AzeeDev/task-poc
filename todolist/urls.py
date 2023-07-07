from todolist import views
from django.urls import path

urlpatterns = [
    path('', views.ItemsView.as_view(), name='home'),
]
