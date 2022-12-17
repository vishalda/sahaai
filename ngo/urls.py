"""PhotoStall URL Configuration

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
from . import views
from django.urls import path


urlpatterns = [
    path('',views.index,name="index"),
    path('register-ngo/',views.register_ngo,name="Register NGO"),
    path('login-ngo/',views.login_ngo,name="Login NGO"),
    path('logout-ngo/',views.logout_ngo,name="Logout NGO"),
    path('ngo/<int:nid>/',views.ngo_page,name="NGO page"),
    path('donation/<int:nid>/',views.get_qrCode,name="QR Code"),
    path('donate-list/',views.donateList,name="Donate List")

]
