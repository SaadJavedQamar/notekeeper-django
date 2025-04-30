

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
def index(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})

def add_note(request):
    if request.method == 'POST':
        Note.objects.create(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('home')
    return render(request, 'notes/add_note.html')  # ✅ correct path


def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('home')


def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit_note.html', {'form': form})