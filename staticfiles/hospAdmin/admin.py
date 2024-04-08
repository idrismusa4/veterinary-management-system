from django.contrib import admin

from .models import Session,Appointment,Admin
# Register your models here.
admin.site.register(Appointment)
admin.site.register(Admin)
admin.site.register(Session)

# Register your models here.