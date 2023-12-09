from django.urls import path
from . import views

urlpatterns = [
    path('note/<int:note_id>', views.note, name='note'),
    path('delete_note/<int:note_id>', views.delete_note, name='delete-note'),
]
