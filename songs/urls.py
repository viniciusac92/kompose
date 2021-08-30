from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import SongView

app_name = 'kompose'
router = SimpleRouter()
router.register(r'songs', SongView.as_view(), basename='songs')
router.register(r'songs/<int:song_id>/', SongView.as_view(), basename='songs2')

urlpatterns = router.urls
