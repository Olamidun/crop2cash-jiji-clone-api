import pytest
import tempfile
from django.contrib.auth import get_user_model
from django.conf import settings
from seller.factory.factories import SellerFactory
from items.models import Items
from pytest_factoryboy import register
from django.core.files.uploadedfile import SimpleUploadedFile



register(SellerFactory, "registered_user")

Seller = get_user_model()
@pytest.fixture()
def register_seller():
    seller = Seller.objects.create(
        first_name="John",
        last_name="Doe",
        email="johndoe@gmail.com",
        )
    
    seller.set_password("vision2022")
    seller.save()
    return seller

@pytest.fixture()
def seller_token(register_seller, client):
    response = client.post(
        "/sellers/login", 
        {"email": register_seller.email, "password": "vision2022"}
    )

    return {"HTTP_AUTHORIZATION": f"Bearer {response.json()['access']}", "Content-Type": "multipart/form-data"}

@pytest.fixture()
def seller_invalid_token(register_seller, client):
    response = client.post(
        "/sellers/login", 
        {"email": register_seller.email, "password": "vision2022"}
    )

    return {"HTTP_AUTHORIZATION": f"Bearer {response.json()['access']}mklkk", "Content-Type": "multipart/form-data"}


@pytest.fixture()
def item(register_seller):
    item = Items.objects.create(
        name="An Item",
        seller=register_seller,
        price=15000.55,
        description="This is a random item",
        image=tempfile.NamedTemporaryFile(suffix=".jpg").name
    )
    return item