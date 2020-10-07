from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('about', views.about, name="about"),
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name="contact"),
    path('single', views.single, name="single"),
    path('single2', views.single2, name="single2"),
    path('single3', views.single3, name="single3"),
    path('single4', views.single4, name="single4"),
    path('single5', views.single5, name="single5"),
    path('single6', views.single6, name="single6"),
]