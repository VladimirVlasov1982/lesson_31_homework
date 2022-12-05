import pytest


# Тест на выдачу одного объявления
@pytest.mark.django_db
def test_ad_retrieve(client, ads, access_token):
    expected_response = {
        "id": ads.pk,
        "name": "test name",
        "author": ads.author_id.username,
        "category": ads.category_id.name,
        "price": 2500,
        "description": "test",
        "is_published": False,
        "image": None,

    }
    response = client.get(f"/ad/{ads.pk}/", HTTP_AUTHORIZATION="Bearer " + access_token)
    assert response.status_code == 200
    assert response.data == expected_response
