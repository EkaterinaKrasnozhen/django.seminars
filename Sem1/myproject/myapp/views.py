from django.shortcuts import render
import logging
from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
 return HttpResponse("Hello, world!")


def about(request):
 return HttpResponse("About us")