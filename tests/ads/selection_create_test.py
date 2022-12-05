import pytest


# Тест на создание подборки
@pytest.mark.django_db
def test_selection_create(client, access_token, ads):
    expected_response = {
        "id": 1,
        "name": "selection test",
        "owner": "test1",
        "items": [ads.pk]
    }

    data = {
        "name": "selection test",
        "items": [ads.pk],
    }

    response = client.post(
        "/selection/create/",
        data=data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + access_token
    )

    assert response.status_code == 201
    assert response.data == expected_response
