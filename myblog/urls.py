"""myblog URL Configuration

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
from django.urls import path,include
from myblog import views
from django.views.static import serve
from django.conf.urls import url
admin.site.site_header="Arpit Jain is Admin"
admin.site.site_title="CodeSmashers Admin Panel"
admin.site.index_title="Welcome to CodeSmashers Admin Panel"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('myblog/', include('home.urls')),

]
