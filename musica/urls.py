from rest_framework import routers
from .views import AlbumViewSet, MusicianViewSet

router = routers.SimpleRouter()
router.register(r'api/v1/albumes', AlbumViewSet)
router.register(r'api/v1/ausians', MusicianViewSet)