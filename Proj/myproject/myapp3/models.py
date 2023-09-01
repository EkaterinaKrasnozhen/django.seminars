from collections import deque
from django.db import models
from random import randint


class Kicks(models.Model):
    result = models.BooleanField()
    kicktime = models.DateTimeField(auto_now=True)
    
    @staticmethod
    def statistic(n: int) -> dict:
        reshka = 0
        eagle = 0
        for _ in range(n):
            kick = Kicks(result=randint(0,1))  
            if kick.result:
                reshka += 1
            else:
                eagle += 1
        res_dict = {
            'орел': eagle,
            'решка': reshka
            }
        return res_dict
    
    @staticmethod
    def count_n(n: int) -> dict:
        coins = deque(Kicks.objects.all(), maxlen=n)
        res = {'reshka': 0, 'eagles': 0}
        for coin in coins:
            if coin.result:
                res['reshka'] += 1
            else:
                res['eagles'] += 1
        return res
    

class Author(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birth = models.DateField()
    fullname = f'{lastname} {name}'
    
    def __str__(self):
        return f'Fullname: {self.fullname}, email: {self.email}, birth: {self.birth}'
                  

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views_count = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Title is {self.title}'
    