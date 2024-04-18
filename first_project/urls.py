"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('', include('login.urls')),
    path('', include('forgot.urls')),
    path('', include('verifypassword.urls')),
    path('', include('resetpassword.urls')),
    path('', include('newpassword.urls')),
    path('', include('home.urls')),
    path('', include('sitterform.urls')),
    path('', include('newsitter.urls')),
    path('', include('sitterduty.urls')),
    path('', include('babyform.urls')),
    path('', include('newbaby.urls')),
    path('', include('babycheck.urls')),
    path('', include('sales.urls')),
    path('', include('supply.urls')),
    path('', include('invent.urls')),
    
]

