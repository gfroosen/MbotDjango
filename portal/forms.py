from django import forms

from .models import Robot

class PostForm(forms.ModelForm):

    class Meta:
        model = Robot
        fields = ('motorspeedright', 'motorspeedleft',)
