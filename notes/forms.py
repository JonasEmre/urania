from django import forms


class CreateNoteForm(forms.Form):
    title = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'note-form__title'}))
    content = forms.CharField(max_length=3000,
                              widget=forms.Textarea(attrs={'placeholder': 'Content', 'class': 'note-form__content'}))
