from django.urls import path
from .views import NoteListCreateView, NoteListDeleteView

urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note-list'),
    path('notes/delete/<int:pk>', NoteListDeleteView.as_view(), name='delete-note'),
]
