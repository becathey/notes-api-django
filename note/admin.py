from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "text")

admin.site.register(Note, NoteAdmin)