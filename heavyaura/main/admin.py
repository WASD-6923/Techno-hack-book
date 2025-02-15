from django.contrib import admin
from .models import Soldat, Geroy


@admin.register(Soldat)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Geroy)
class GeroyAdmin(admin.ModelAdmin):
    list_display = ['name','slug','age','available','created','updated']
    list_filter = ['available','created', 'updated']
    list_editable = ['age','available']
    prepopulated_fields = {'slug':('name',)}

