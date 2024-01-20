from django.contrib import admin
from .models import *

class MashAdmin(admin.ModelAdmin):
    pass

class MunAdmin(admin.ModelAdmin):
    pass

class ComAdmin(admin.ModelAdmin):
    pass

class CommentInline(admin.TabularInline):
    model=Comment
    extra=1

class MashqInline(admin.ModelAdmin):
    inlines=[CommentInline]

admin.site.register(Mashqlar,MashqInline)
admin.site.register(Mundarija,MunAdmin)
admin.site.register(Comment,ComAdmin)
