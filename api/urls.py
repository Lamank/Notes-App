from django.urls import path
from api import views

urlpatterns = [
    path('', views.getRoutes, name='route'),
    path('notes/', views.getNotes, name='notes'),
    path('notes/create/', views.createNote, name='new_notes'),
    path('notes/<int:pk>/update/', views.updateNote, name='update_note'),
    path('notes/<int:pk>/delete/', views.deleteNote, name='delete_note'),

    path('notes/<int:pk>/', views.getNote, name='get_note'),

]
