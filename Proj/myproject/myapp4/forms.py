from django import forms
from .models import Author


class GameForm(forms.Form):
    game = forms.ChoiceField(choices=[('1', 'Кубик'), ('2', 'Случайное число'), ('3', 'Монетка')])
    count = forms.IntegerField(min_value=1, max_value=64)


class AuthorForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    
    
class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.TextInput())
    author = forms.ModelChoiceField(queryset= Author.objects.all())
