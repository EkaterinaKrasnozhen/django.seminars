from random import choices, randint
from django.core.management.base import BaseCommand
from myapp4.models import Author, Post, Comment

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. " \
        "Accusamus accusantium aut beatae consequatur consequuntur cumque, delectus et illo iste maxime " \
        "nihil non nostrum odio officia, perferendis placeat quasi quibusdam quisquam quod sunt " \
        "tempore temporibus ut voluptatum? A aliquam culpa ducimus, eaque eum illo mollitia nemo " \
        "tempore unde vero! Blanditiis deleniti ex hic, laboriosam maiores odit officia praesentium " \
        "quae quisquam ratione, reiciendis, veniam. Accusantium assumenda consectetur consequatur " \
        "consequuntur corporis dignissimos ducimus eius est eum expedita illo in, inventore " \
        "ipsum iusto maiores minus mollitia necessitatibus neque nisi optio quasi quo quod, " \
        "quos rem repellendus temporibus totam unde vel velit vero vitae voluptates."


class Command(BaseCommand):
    help = "Generate commits."
    
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Commit ID')
        
    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count+1):
            author = Author.objects.filter(pk=i).first()
            posts = Post.objects.filter(author=author)
            for post in posts:
                comment = Comment(author=author, post=post, comment=" ".join(choices(text, k=25)))
                comment.save()