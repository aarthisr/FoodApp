from django.urls import path, include
from . import views

app_name="Food"
urlpatterns=[
    # path('', views.index, name='index'),
    path('', views.IndexItemList.as_view(), name='index'),
    path('item/', views.item, name='Item'),
    # path('<int:item_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    # path('add/', views.create_item, name='create_item'),
    path('add/', views.FoodCreate.as_view(), name='create_item'),
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]