from django.urls import include, path
# from rest_framework import routers
from .views import signup_response_list

# from .views import SignupResponseViewSet

# router = routers.DefaultRouter()
# router.register(r'signups', SignupResponseViewSet)

app_name = 'api_v1'
urlpatterns = [
    # path('', include(router.urls)),
    path('signups/', signup_response_list, name='signup_list'),
]
