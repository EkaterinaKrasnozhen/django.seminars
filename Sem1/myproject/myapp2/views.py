from random import randint
from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def text(title, result):
    return f'<h1>{title}<h1>' \
        f'<p> Результат для вас: {result}<p>'
        
        
def coin(request):
    title = 'Бросок монеты'
    res = ''
    temp = randint(1, 2)
    if temp == 1:
        res = 'решка'
    else:
        res = 'орел'
        
    logger.info(f'Сгенерированное значение - {res}')
    return HttpResponse(text(title, res))
        
        
def cube(requset):
    title = 'Бросок кубика'
    res = randint(1, 6)
    logger.info(f'Сгенерированное значение - {str(res)}')
    return HttpResponse(text(title, res))

 
