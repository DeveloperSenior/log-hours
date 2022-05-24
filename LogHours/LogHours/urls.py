"""LogHours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from LogHoursApp import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('log/', views.log, name='log'),
    path('log/show/all', views.show_all, name='log/show/all'),
    path('log/show', views.show, name='log/show'),
    path('log/edit/<int:id>', views.edit, name='log/edit'),
    path('log/edit/update/<int:id>', views.update, name='log/update'),
    path('log/delete/<int:id>', views.destroy, name='log/delete'),
    path('log/import/', views.import_data, name="log/import"),
]

admin.site.site_header = 'Registro de horas'
admin.site.index_title = 'Registro horas'
admin.site.site_title = 'Administrar'
