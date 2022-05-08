import pytest
from django.contrib.auth import get_user_model
from django.conf import settings
from seller.factory.factories import SellerFactory
from pytest_factoryboy import register

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
    return seller.email

@pytest.fixture()
def seller_token(register_seller, client):
    response = client.post(
        "/seller/login", 
        {"email": register_seller.email, "password": "vision2022"}
    )

    return {"Authorization": f"Bearer {response.json()['access']}"}