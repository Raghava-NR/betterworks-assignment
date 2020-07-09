from analytics import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'objectives', views.ObjectivesViewSet, base_name='ObjectivesViewSet')

urlpatterns = router.urls
