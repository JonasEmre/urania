from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Note

# Create your views here.
def note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'notes/note.html', {'note': note})


def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if note:
        note.delete()
        messages.success(request, 'Note deleted')
        return redirect('profile')
