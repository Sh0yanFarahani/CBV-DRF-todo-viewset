from rest_framework.routers import SimpleRouter, DefaultRouter
from django.urls import path
from .views import TaskViewSet

app_name = 'api-v1'

router = DefaultRouter()
router.register('task', TaskViewSet, basename='tasks')
urlpatterns = router.urls
