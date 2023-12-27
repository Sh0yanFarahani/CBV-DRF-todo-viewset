from django.contrib import admin

# Register your models here.


from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    model = Todo
    list_display = (
        'title',
        'body',
    )
    list_filter = ('title', 'body',)
    search_fields = ('title',)
    ordering = ("title",)

admin.site.register(Todo, TodoAdmin)