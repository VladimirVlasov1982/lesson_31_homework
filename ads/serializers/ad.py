from rest_framework import serializers
from ads.models import Ads, Categories
from users.models import User


class CategoriesViewSerializer(serializers.ModelSerializer):
    """Сериализатор категорий"""

    class Meta:
        model = Categories
        fields = "__all__"


class AdsListSerializer(serializers.ModelSerializer):
    """Сериализатор объявлений"""

    class Meta:
        model = Ads
        fields = "__all__"


class AdsDetailSeraializer(serializers.ModelSerializer):
    """Сериализатор вывода одного объявления"""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
        source="author_id"
    )
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name",
        source="category_id"
    )

    class Meta:
        model = Ads
        exclude = ["author_id", "category_id"]


class AdsCreateSerializer(serializers.ModelSerializer):
    """Сериализатор создания объявления"""
    id = serializers.IntegerField(required=False)
    author_id = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field="pk",
    )
    category_id = serializers.SlugRelatedField(
        required=False,
        queryset=Categories.objects.all(),
        slug_field="pk",
    )

    def validate_is_published(self, value):
        if value == True:
            raise serializers.ValidationError("Значение поля is_published должно быть false")
        return value

    class Meta:
        model = Ads
        fields = "__all__"


class AdsUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор обновления объявления"""
    author_id = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field="pk"
    )
    category_id = serializers.SlugRelatedField(
        required=False,
        queryset=Categories.objects.all(),
        slug_field="pk"
    )

    class Meta:
        model = Ads
        fields = "__all__"


class AdsDeleteSerializer(serializers.ModelSerializer):
    """Сериализатор удаления объявления"""

    class Meta:
        model = Ads
        fields = ["id"]
