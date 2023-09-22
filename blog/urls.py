from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('category/<slug:slug>/', views.CategoriesView.as_view(), name='category-list'),
]
