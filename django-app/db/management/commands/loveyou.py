from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'This command'

    def add_arguments(self, parser):

        parser.add_argument("--times", help="testing")

    def handle(self, *args, **options):

        times = options.get("times")

        for t in range(0, int(times)):

            print("I Love You")
