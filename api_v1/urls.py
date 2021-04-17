from django.urls import include, path
from rest_framework import routers

from .views import SignupResponseViewSet

router = routers.DefaultRouter()
router.register(r'signups', SignupResponseViewSet)

app_name = 'api_v1'
urlpatterns = [
    path('', include(router.urls)),
]
