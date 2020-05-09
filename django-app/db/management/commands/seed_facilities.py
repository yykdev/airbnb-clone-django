from django.core.management.base import BaseCommand
from db.models import Facility


class Command(BaseCommand):

    help = 'This Custom Facility Command'

    # def add_arguments(self, parser):
    #
    #     parser.add_argument("--times", help="testing")

    def handle(self, *args, **options):

        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for f in facilities:

            Facility.objects.create(name=f)

        self.stdout.write(self.style.SUCCESS("{} Facility created!".format(len(facilities))))
