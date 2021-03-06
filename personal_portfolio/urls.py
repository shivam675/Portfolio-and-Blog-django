"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls'), name='blogs'),
    path('signupuser', views.signupuser, name='signupuser'),
    path('loginuser', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('gsoc2021/python-challenge/', views.gsoc2021, name = 'gsoc_python'),
    path('gsoc2021/roboticsAcademychallenge', views.roboticsAcademychallenge, name='gsoc_acad'),
    path('base/', views.base, name='base'),
    path('major-projects/', views.major_projects, name='major_projects'),
    path('contact-me/', views.contact_me, name='contact'),
    path('my-certifications', views.certification, name='certification'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
