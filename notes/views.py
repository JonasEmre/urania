from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Note
from .forms import UpdateNoteForm

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


def update_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == 'POST':
        form = UpdateNoteForm(request.POST, initial={
                              'title': note.title, 'content': note.content})
        if form.is_valid():
            note.title = form.cleaned_data.get('title')
            note.content = form.cleaned_data.get('content')
            note.save()
            messages.success(request, 'You updated your note.')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid note')
    else:
        form = UpdateNoteForm(
            initial={'title': note.title, 'content': note.content})
    return render(request, "notes/update-note.html", {'note': note, 'form': form})
