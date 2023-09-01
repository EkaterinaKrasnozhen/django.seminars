import datetime
from random import randint
from django.core.management.base import BaseCommand
from myapp3.models import Post, Author


class Command(BaseCommand):
    help = "Generate fake posts."
    
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Posts ID')
    
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        authors = Author.objects.all()
        for j in range(1, count + 1):
            for author in authors:
                post = Post(
                    title=f'Title{j}', 
                    content=f'Text from {author.name} #{j} is bla bla bla many long text', 
                    date=datetime.datetime.now(),
                    author=author,
                    category='детская',
                    views_count = j, 
                    publish=randint(0,1)
                )
                post.save()