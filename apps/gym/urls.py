from rest_framework.routers import DefaultRouter

from .views import GymViewset, OrderViewset

router = DefaultRouter()
router.register('order', OrderViewset)
router.register('', GymViewset)



urlpatterns = []
urlpatterns += router.urls