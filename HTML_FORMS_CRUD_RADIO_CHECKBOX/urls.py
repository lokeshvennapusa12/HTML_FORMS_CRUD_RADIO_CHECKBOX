"""HTML_FORMS_CRUD_RADIO_CHECKBOX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Insert_topic/',Insert_topic,name='Insert_topic'),
    path('Insert_webpage/',Insert_webpage,name='Insert_webpage'),
    path('insert_access/',insert_access,name='insert_access'),
    path('retrieve/',retrieve,name='retrieve'),
    path('checkbox/',checkbox,name='checkbox'),
    path('radio/',radio,name='radio'),
    path('retrieve_access/',retrieve_access,name='retrieve_access'),
    path('update_webpage/',update_webpage,name='update_webpage'),
    
]
