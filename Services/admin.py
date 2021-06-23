from django.contrib import admin
from Services.models import Service

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated',)
    list_display = ('title', 'content',)
    search_fields = ('title',)


admin.site.register(Service, ServiceAdmin)


