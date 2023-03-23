from django.urls import path
from api import views

urlpatterns = [
    # path('', views.getRoutes, name='route'),
    path('notes/', views.getNotes, name='Notes'),

    path('notes/<int:pk>/', views.getNote, name='Note'),

]
