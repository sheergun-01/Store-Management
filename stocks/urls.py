from django.urls import path
from . import views

app_name = 'stocks'
urlpatterns = [
    path('',views.index,name='index'),
    path('item_list/',views.item_list,name='item_list'),
    path('update_item/<str:pk>/',views.update_item,name='update_item'),
    path('delete_item/<str:pk>/', views.delete_item, name="delete_item"),
    path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
    path('add_item/',views.add_item,name='add_item'),
    path('issue_item/<str:pk>/', views.issue_item, name="issue_item"),
    path('receive_item/<str:pk>/', views.receive_item, name="receive_item"),
    path('reorder_level/<str:pk>/', views.reorder_level, name="reorder_level"),
]