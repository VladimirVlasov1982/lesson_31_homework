import pytest


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = "test1"
    password = "123qwe"


    django_user_model.objects.create_user(
        username=username,
        password=password,
        role="Администратор",
    )

    response = client.post(
        "/user/token/",
        data={"username": username, "password": password},
        content_type="application/json"
    )

    return response.data["access"]
