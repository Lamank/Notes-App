from django.contrib import admin
from api.models import Note


class NoteModelAdmin(admin.ModelAdmin):
    list_display = ('body', 'created', 'updated',)
    list_display_links = ('body', )
    readonly_fields = ("created", "updated",)
    list_filter = ("created", "body", "updated",)
    empty_value_display = 'unknown'
    search_fields = ("body",)
    
admin.site.register(Note, NoteModelAdmin)

