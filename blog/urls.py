
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,),
    path('',views.index,name='index'),
    path('author/',include('author.urls')),
    path('post/',include('posts.urls')),
    path('category',include('categories.urls')),
    path('profile/',include('profiles.urls')),
]
