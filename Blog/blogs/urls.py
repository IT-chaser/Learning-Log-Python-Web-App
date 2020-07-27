"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page taht shows all blogs.
    path('blogs/', views.blogs, name='blogs'),
    # Detail page for a single blog
    path('blogs/<int:blog_id>/', views.blog, name='blog' )
    # Page for adding a new blog
    path('new_post/', views.new_post, name='new_post'),
    # Page for editing an entry.
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]
