from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('<slug:slug_text>', views.post_detail, name='post'),
    path('category/<slug:cat_slug>', views.post_category_list, name='category'),
]