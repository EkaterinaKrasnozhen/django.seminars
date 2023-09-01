from django.core.management.base import BaseCommand
from myapp3.models import Author


class Command(BaseCommand):
    help = "Generate fake authors."
    
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Author ID')
    
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Kate{i}', lastname='Kras', email=f'{i}@example.com', biography='Born in Moscow', birth='1984-12-25')
            author.save()