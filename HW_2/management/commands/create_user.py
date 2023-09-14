from django.core.management.base import BaseCommand

from HW_2.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='John', email='john@example.com', phone='89076543234', address='Moscow City',

                    registered_at='01.01.2001')

        user.save()

        self.stdout.write(f'{user}')


