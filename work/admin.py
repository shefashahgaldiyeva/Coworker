from django.contrib import admin
from .models import Work

# Register your models here.

# admin.site.register(Work)

@admin.register(Work)

class WorkAdmin(admin.ModelAdmin):
    class Meta:
        model = Work

    list_display = ['title','author']
    list_display_links = ['title','author']
    search_fields = ['title','create_date']
    list_filter = ['title']