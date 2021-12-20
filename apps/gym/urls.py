from rest_framework.routers import DefaultRouter

from .views import GymViewset

router = DefaultRouter()
router.register('', GymViewset)


urlpatterns = []
urlpatterns += router.urls