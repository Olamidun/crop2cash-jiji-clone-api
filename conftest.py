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
    return seller