import random

from django.core.management.base import BaseCommand
from django_seed import Seed

from db.models import User, Room, RoomType


class Command(BaseCommand):

    help = 'This Custom Room Command'

    def add_arguments(self, parser):

        parser.add_argument("--number", default=1, type=int, help="testing")

    def handle(self, *args, **options):

        number = options.get("number")
        seeder = Seed.seeder()

        all_users = User.objects.all()
        room_types = RoomType.objects.all()

        seeder.add_entity(Room, number, {
            'name': seeder.faker.address(),
            'host': lambda x: random.choice(all_users),
            'room_type': lambda x: random.choice(room_types),
            'guests': lambda x: random.randint(1, 10),
            'price': lambda x: random.randint(10, 300),
            'beds': lambda x: random.randint(1, 5),
            'bedrooms': lambda x: random.randint(1, 5),
            'baths': lambda x: random.randint(1, 5),
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS("{} Room created!".format(number)))
