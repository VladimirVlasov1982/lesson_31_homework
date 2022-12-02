from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from users.models import User, Locations
from users.serializers import UsersListSerializer, UsersDetailSerializer, UsersCreateSerializer, UsersUpdateSerializer, \
    UsersDeleteSerializer, LocationsSerializer


class LocationsViewSet(ModelViewSet):
    """Содержит в себе все базовые API-методы для локаций"""
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer


class UsersListView(ListAPIView):
    """Возвращает всех пользователей"""
    queryset = User.objects.all()
    serializer_class = UsersListSerializer


class UsersDetailView(RetrieveAPIView):
    """Возвращает пользователя по его id"""
    queryset = User.objects.all()
    serializer_class = UsersDetailSerializer


class UsersCreateView(CreateAPIView):
    """Создает пользователя"""
    model = User
    serializer_class = UsersCreateSerializer


class UsersUpdateView(UpdateAPIView):
    """Обновляет пользователя"""
    queryset = User.objects.all()
    serializer_class = UsersUpdateSerializer


class UsersDeleteView(DestroyAPIView):
    """Удаляет пользователя"""
    queryset = User.objects.all()
    serializer_class = UsersDeleteSerializer

