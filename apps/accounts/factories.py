from django.contrib.auth.hashers import make_password
from factory import Faker, LazyFunction, Sequence
from factory.django import DjangoModelFactory

from .models import CustomUser


class UserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser

    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    username = Sequence(lambda x: f"user{x}")
    email = Sequence(lambda x: f"user{x}@example.com")
    password = LazyFunction(lambda: make_password("pi3.1415"))
