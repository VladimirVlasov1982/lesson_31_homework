import pytest

# Тест на создание объявления
@pytest.mark.django_db
def test_ad_create(client, categories, user):
    expected_response = {
        "id": 1,
        "author_id": 1,
        "category_id": 1,
        "name": "Стол из слэба",
        "price": 24000,
        "description": "123",
        "is_published": False,
        "image": None
    }

    data = {
        "name": "Стол из слэба",
        "price": 24000,
        "description": "123",
        "is_published": False,
        "category_id": categories.pk,
        "author_id": user.pk,
    }

    response = client.post("/ad/create/", data=data, content_type="application/json")

    assert response.status_code == 201
    assert response.data == expected_response
