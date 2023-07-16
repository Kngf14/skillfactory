from django.contrib import admin
from .models import Callboard, Category, Reply

admin.site.register(Callboard)
admin.site.register(Category)

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('text', 'datetime_created', 'user', 'callb', 'approved')
    list_filter = ('approved', 'datetime_created')
    search_fields = ('user', 'text')

    def approve_reply(self, request, queryset):
        queryset.update(approve=True)


admin.site.register(Reply, ReplyAdmin)
