from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from apps.accounts.factories import UserFactory

from .models import Post


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    author = SubFactory(UserFactory)
    title = Faker("sentence", nb_words=2)
    body = Faker("sentence", nb_words=60)
