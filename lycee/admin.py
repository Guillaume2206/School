from django.contrib import admin
from .models import Student,Cursus,Presence,CallOfRoll

admin.site.site_header="Admin Page"
# Register your models here.
class studentAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "email", 'phone' )

class CursusAdmin(admin.ModelAdmin):
  fields = ["scholar_year","name","year_from_bac"]

class PresenceAdmin(admin.ModelAdmin):
  fields = ["student","date","dayhalf","reason"]

class CallOfRollAdmin(admin.ModelAdmin):
  fields = ["student","date","dayhalf","isPresent"]

admin.site.register(Student,studentAdmin)
admin.site.register(Cursus,CursusAdmin)
admin.site.register(Presence,PresenceAdmin)
admin.site.register(CallOfRoll,CallOfRollAdmin)
