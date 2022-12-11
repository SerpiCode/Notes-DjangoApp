from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView, name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('create-note/', CreateNoteView.as_view(), name='create-note'),
    path('notes/', NotesView.as_view(), name='notes'),
    path('edit-note/<int:pk>', EditNoteView.as_view(), name='edit-note'),
    path('delete-note/<int:pk>', DeleteNoteView.as_view(), name='delete-note'),
]