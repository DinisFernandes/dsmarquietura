from django.contrib import admin
from .models import Projeto, Contact, GaleriaPhotos, Testemunho

# Register your models here.

class PhotosInline(admin.StackedInline):
    model = GaleriaPhotos
    extra = 1

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'data_post')
    list_display_links = ('id', 'title')
    inlines = [PhotosInline]

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'tratado', 'data_contact')
    list_editable = ['tratado',]


class TestemunhoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Testemunho, TestemunhoAdmin)