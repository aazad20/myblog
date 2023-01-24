from django.urls import path,include
from .views import BlogListView,BlogDetailView,BlogCreateView


urlpatterns = [
    path('', BlogListView.as_view(),name="index"),
    path('blog/<int:pk>', BlogDetailView.as_view(),name="blogdetail"),
    path('add/', BlogCreateView.as_view(),name="addblog"),

]
