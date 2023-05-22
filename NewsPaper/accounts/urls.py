from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostUpdate, PostDelete, PostCreate, CategoryListView, subscribe, HelloView
from django.core.cache import cache
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('', cache_page(60)(PostList.as_view()), name='post_list'),
   path('<int:pk>', cache_page(300)(PostDetail.as_view()), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('hello', HelloView.as_view(), name='hello'),
]