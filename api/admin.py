from django.contrib import admin
from api.models import Note


class NoteModelAdmin(admin.ModelAdmin):
    list_display = ('body', 'created', 'updated',)
    
admin.site.register(Note, NoteModelAdmin)

