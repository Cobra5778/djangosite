"""djangosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from mysite import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/', views.logins, name='logins'),
    path('logout/', views.logouts, name='logouts'),
    path('yandex_ac493dcd5af1d1e6.html/', views.yandex_63a3d0a896e29e17, name='yandex_63a3d0a896e29e17'),
    path('<int:id_arc_tree>/', views.site_main_new, name='site_main'),
    path('<int:id_arc_tree>-<str:article_name>/', views.site_main_new, name='site_main'),
    path('<str:article_name>/', views.site_main_new, name='site_main'),
    path('', views.site_main_new, name='site_main'),
]
