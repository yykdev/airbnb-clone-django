from django.core.management.base import BaseCommand
from django_seed import Seed

from db.models import User


class Command(BaseCommand):

    help = 'This Custom Users Command'

    def add_arguments(self, parser):

        parser.add_argument("--number", default=1, type=int, help="testing")

    def handle(self, *args, **options):

        number = options.get("number")
        seeder = Seed.seeder()

        seeder.add_entity(User, number, {
            'is_staff': False,
            'is_superuser': False,
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS("{} Users created!".format(number)))
