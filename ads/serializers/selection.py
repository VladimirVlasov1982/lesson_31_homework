from rest_framework import serializers
from ads.models import Selection
from ads.serializers.ad import AdsDetailSeraializer


class SelectionListSerializer(serializers.ModelSerializer):
    """Сериализатор подборок"""

    class Meta:
        model = Selection
        fields = ["id", "name"]


class SelectionDetailSerializer(serializers.ModelSerializer):
    """Сериализатор одной подборки"""
    items = AdsDetailSeraializer(many=True)

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionCreateSerializer(serializers.ModelSerializer):
    """Сериализатор создания подборки"""
    id = serializers.IntegerField(required=False)
    owner = serializers.SlugField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор обновления подборки"""

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionDeleteSerializer(serializers.ModelSerializer):
    """Сериализатор удаления подборки"""

    class Meta:
        model = Selection
        fields = "id"
