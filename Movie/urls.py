"""
URL configuration for Movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('movieadd/', MovieAddView.as_view(), name='movieadd'),
    path('movielist/',MovieListView.as_view(),name='movielist'),
    path('moviedelete/<int:pk>',MovieDeleteView.as_view(),name='moviedelete'),
    path('movieupdate/<int:pk>',MovieUpdateView.as_view(),name='movieupdate'),
    path('moviedetails/<int:pk>',MovieDetailView.as_view(),name="moviedetails"),
    path('reviewadd/<int:pk>',ReviewAddView.as_view(),name='reviewadd'),
    path('reviewupdate/<int:pk>',ReviewUpdateView.as_view(),name='reviewupdate'),
    path('reviewlist/<int:pk>',ReviewListView.as_view(),name='reviewlist'),
    path('reviewdelete/<int:pk>',ReviewDeleteView.as_view(),name='reviewdelete'),
    path('reviewuserlist/<int:pk>',ReviewUserlistView.as_view(),name='reviewuserlist'),
    path('genrelist/<str:pk>',Genrelist.as_view(),name="genrelist"),
    path('search/', SearchView.as_view(), name='search'),
    path('logout/', Logout.as_view(), name='logout'),
    path('',Homepage.as_view()),
    path('userdetails/<int:pk>',userdetails.as_view(),name='userdetails'),
    path('admindetails/<int:pk>',admindetails.as_view(),name='admindetails'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

