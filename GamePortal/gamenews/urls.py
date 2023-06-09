from django.urls import path

from .views import (CallList, CallCreate, CallUpdate, CallDelete, CategoryListView, call_detail_view)

urlpatterns = [
    path('', CallList.as_view(), name='call_list'),
    path('<int:pk>', call_detail_view, name='call_detail'),
    path('create/', CallCreate.as_view(), name='call_create'),
    path('<int:pk>/edit/', CallUpdateView.as_view(), name='call_edit'),
    path('replies/<int:pk>/delete/', CallDeleteView.as_view(), name='call_delete'),
    path('category/<int:pk>', CategoryListView.as_view(), name='category_list'),
]