from todolist import views
from django.urls import path

urlpatterns = [
    path('', views.ItemsView.as_view(), name='home'),
    path('item/<int:pk>/', views.AddEditItemsView.as_view(), name='add-edit-item'),
    path('delete-item/<int:pk>/', views.DeleteItemsView.as_view(), name='delete-item'),

]
