from django.contrib import admin
from service.models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_title', 'service_author', 'service_description')

admin.site.register(Service, ServiceAdmin)    