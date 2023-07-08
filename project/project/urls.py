"""project URL Configuration

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
from Sprint import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .yasg import urlpatterns as doc_urls

from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'coords', views.CoordsViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'levels', views.LevelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api1/', include(router.urls)),
    path('swagger-ui/', TemplateView.as_view(template_name = 'swagger-ui.html', extra_context = {'schema_url': 'openapi-schema'}), name='swagger'),
    path('openapi/', get_schema_view(title="Pass", description="Pass application API", version="0.1",), name='openapi-schema'),
]

urlpatterns += doc_urls

# Api routers

