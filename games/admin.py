from django.contrib import admin
from games.models import Choice, Game

class ChoiceInline(admin.TabularInline):
    model = Choice

class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    # list_display - a tuple of field names to display, as columns
    list_display = ('question', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

admin.site.register(Game, GameAdmin)
