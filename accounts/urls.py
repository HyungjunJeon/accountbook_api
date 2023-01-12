from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.account_create),
    path('', views.account_list, name='account_list'),
    path('<int:pk>', views.account_detail, name='account_detail'),
    path('update/<int:pk>', views.account_update, name='account_update'),
    path('delete/<int:pk>', views.account_delete, name='account_delete'),
]