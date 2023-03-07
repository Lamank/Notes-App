from django.urls import path
from api import views

urlpatterns = [
    path('', views.getRoutes, name='route'),
    path('notes/', views.getNotes, name='notes'),
    path('notes/<int:pk>', views.getNote, name='note'),

]
