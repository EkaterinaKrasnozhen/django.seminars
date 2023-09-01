from django.core.management.base import BaseCommand
from myapp3.models import Author


class Command(BaseCommand):
    help = "Create author."
    
    def handle(self, *args, **kwargs):
        author = Author(name='Kate', lastname='Kras', email='neo@example.com', biography='Born in Moscow', birth='1985-12-23')

        author.save()
        self.stdout.write(f'{author}')