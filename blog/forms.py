from django.forms import widgets

from .models import Comment
from django import forms


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'rating')

        widgets = {
            'next': forms.TextInput(attrs={'class': 'form-control'})
        }
