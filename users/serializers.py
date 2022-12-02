from django.db.models import Count, Q
from rest_framework import serializers
from users.models import User, Locations


class LocationsSerializer(serializers.ModelSerializer):
    """Сериализатор локаций"""

    class Meta:
        model = Locations
        fields = '__all__'


class UsersListSerializer(serializers.ModelSerializer):
    """Сериализатор пользователей"""
    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
        source="location_id"
    )
    total_ads = serializers.SerializerMethodField(method_name="get_total_ads")

    def get_total_ads(self, obj):
        total_ads = obj.ads.aggregate(num=Count("is_published", filter=Q(is_published=True)))["num"]
        return total_ads

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "role", "age", "locations", "total_ads"]


class UsersDetailSerializer(serializers.ModelSerializer):
    """Сериализатор одного пользователя"""
    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
        source="location_id"
    )

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "role", "age", "locations"]


class UsersCreateSerializer(serializers.ModelSerializer):
    """Сериализатор создания пользователя"""
    id = serializers.IntegerField(required=False)
    locations = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Locations.objects.all(),
        slug_field="name",
        source="location_id",
    )

    class Meta:
        model = User
        exclude = ["location_id"]

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop("locations")

        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for location in self._locations:
            location_obj, _ = Locations.objects.get_or_create(name=location)
            user.location_id.add(location_obj)

        user.set_password(validated_data['password'])
        user.save()

        return user


class UsersUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор обновления пользователя"""
    location_id = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Locations.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = User
        exclude = ["password"]

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop("locations", [])

        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save()

        for location in self._locations:
            location_obj, _ = Locations.objects.get_or_create(name=location)
            user.location_id.add(location_obj)

        user.save()
        return user


class UsersDeleteSerializer(serializers.ModelSerializer):
    """Сериализатор удаления пользователя"""

    class Meta:
        model = User
        fields = ["id"]
