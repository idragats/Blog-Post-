from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list_view, name='post_list'),
    path('create/', views.post_create_view, name='post_create'),
    path('update/<int:post_id>/', views.post_update_view, name='post_update'),
    path('delete/<int:post_id>/', views.post_delete_view, name='post_delete'),
    path('search/', views.search_results_view, name='search_results'),  
    path('<int:post_id>/', views.post_detail_view, name='post_detail')
]