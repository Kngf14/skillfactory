from rest_framework import routers
from Sprint import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'mountains', views.MountainsViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]