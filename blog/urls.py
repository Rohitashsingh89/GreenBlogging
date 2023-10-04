from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('blog-details/<slug:post_slug>/', views.blog_details, name="blog_details"),
    path('category/<str:category_slug>/', views.category_posts, name='category_posts'),
]
