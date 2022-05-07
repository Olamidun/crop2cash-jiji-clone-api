import factory
from django.conf import settings
from django.contrib.auth.hashers import make_password


class SellerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL
        _create = ('first_name', 'last_name', 'email', 'state_of_residence', 'password', )

    first_name = 'Olamidun'
    last_name = 'Kolapo'
    email = 'olamidun@gmail.com'
    state_of_residence = 'Oyo'
    password = factory.LazyFunction(lambda: make_password('mkinssnfsidooa'))