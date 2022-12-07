from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Notes
from .forms import SignUpForm, NotesForm, EditNoteForm

# Create your views here.

def HomeView(request):
    username = User.username

    context = {
        'username': username,
    }

    return render(request, 'home.html', context)

class CreateNoteView(generic.CreateView):
    model = Notes
    form_class = NotesForm
    template_name = 'create_note.html'

class EditNoteView(generic.UpdateView):
    model = Notes
    form_class = EditNoteForm
    template_name = 'edit_note.html'

class DeleteNoteView(generic.DeleteView):
    model = Notes
    template_name = 'delete_note.html'
    success_url = reverse_lazy('notes')

class NotesView(generic.ListView):
    model = Notes
    template_name = 'notes.html'
    ordering = ['-date']

    # def get_queryset(self):
    #     return Notes.objects.order_by('date')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
