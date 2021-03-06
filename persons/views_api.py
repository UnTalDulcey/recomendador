from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from persons.models import City, Client, Supervisor
from persons.serializers import UserSerializer, CitySerializer, ClientSerializer, SupervisorSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [SearchFilter, DjangoFilterBackend]
    # search_fields = [
    #     "user__username", "user__first_name", "user__last_name", "user__email"
    # ]
    # filterset_fields = ["person__id",]

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [SearchFilter, DjangoFilterBackend, ]

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [SearchFilter, DjangoFilterBackend, ]

class SupervisorViewSet(viewsets.ModelViewSet):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [SearchFilter, DjangoFilterBackend, ]