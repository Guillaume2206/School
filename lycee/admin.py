from django.contrib import admin
from .models import Student, Cursus

# Register your models here.
admin.site.site_header = "Admin Panel"

admin.site.register(Student)
admin.site.register(Cursus)