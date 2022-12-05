import factory.django
from ads.models import Ads, Categories, Selection
from users.models import User


class CategoriesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categories

    name = "category"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "123qwe"
    email = factory.Faker("name")
    role = "Администратор"


class AdsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ads

    name = "test name"
    author_id = factory.SubFactory(UserFactory)
    category_id = factory.SubFactory(CategoriesFactory)
    price = 2500
    description = "test"
    is_published = False


class SelectionsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Selection

    name = "selection test"
    owner = factory.SubFactory(UserFactory)
    items = factory.SubFactory(AdsFactory)
