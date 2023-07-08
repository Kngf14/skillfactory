from django.contrib import admin
from rest_framework import routers
from Sprint import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'mountains', views.MountainsViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('api2/submit-data/', views.SubmitDataViewSet.as_view(), name = 'create_Mountain'),
    path('api2/submit-data/<int:pk>/', views.PerevalUpdateView.as_view(), name = 'update_Mountain'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)