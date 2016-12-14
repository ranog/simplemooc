"""simplemooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    url(r'^$', views.dashboard, 
        name='dashboard'),

    url(r'^entrar/$', auth_views.login, 
        {'template_name' : 'login.html'}, name='login'),
        #XXX não esquecer de colocar com a extenção: login.html   
 
    url(r'^sair/$', auth_views.logout, 
        {'next_page' : 'home'}, name='logout'),
    
    url(r'^cadastre-se/$', views.register, 
        name='register'),
    
    url(r'^editar/$', views.edit, 
        name='edit'),
    
    url(r'^editar-senha/$', views.edit_password, 
        name='edit_password'),
]

