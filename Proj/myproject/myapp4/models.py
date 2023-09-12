from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Title is {self.title}'
    
    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'
    
    
class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateField(auto_now=True)
    chanched_at = models.DateField(null=True, default=None)