from pytest_factoryboy import register

from tests.factories import CategoriesFactory, AdsFactory, UserFactory

pytest_plugins = "tests.fixtures"

register(CategoriesFactory)
register(UserFactory)
register(AdsFactory)

