from typing import Any
from django import forms
from .models import Note


class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=100, 
                            widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    content = forms.CharField(max_length=3000, 
                            widget=forms.Textarea(attrs={'placeholder': 'Content'}))

    """ class Meta:
        model = Note
        fields = ['title', 'content'] """
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
                self.fields[field].widget.attrs.update({'class': 'form-group__input'})

