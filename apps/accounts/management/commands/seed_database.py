from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from apps.accounts.factories import UserFactory
from apps.posts.factories import PostFactory
from apps.posts.models import Post


class Command(BaseCommand):
    help = "Seed database with sample data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        if Post.objects.exists():
            raise CommandError(
                "This command cannot be run when any post exist, to guard"
                + " against accidental use on production."
            )

        self.stdout.write("Seeding database...")

        create_author_and_post()

        self.stdout.write("Done.")


def create_author_and_post():
    author1, author2, author3 = UserFactory.create_batch(3)

    PostFactory.create_batch(2, author=author1)
    PostFactory.create_batch(3, author=author2)
    PostFactory.create_batch(2, author=author3)
