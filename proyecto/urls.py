from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from musica.views import AlbumViewSet, MusicianViewSet

router = routers.SimpleRouter()
router.register(r'api/v1/albumes', AlbumViewSet)
router.register(r'api/v1/musians', MusicianViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]
