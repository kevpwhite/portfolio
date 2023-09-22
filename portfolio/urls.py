from django.urls import path
from . import views

app_name='portfolio'
urlpatterns = [
    path('', views.PortfolioListView.as_view(), name='portfolio'),
    path('<slug:slug>/', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('category/<slug:slug>/', views.CategoriesView.as_view(), name='category-list'),
]
