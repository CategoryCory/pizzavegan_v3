from rest_framework import viewsets, permissions

from contacts.models import PizzeriaSignupResponse
from contacts.serializers import SignupResponseSerializer


class SignupResponseViewSet(viewsets.ModelViewSet):
    queryset = PizzeriaSignupResponse.objects.all().order_by('restaurant_name')
    serializer_class = SignupResponseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
