from django.contrib import admin
from skill_app.models import Profile, Project

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'city', 'gender', 'pub_date') 

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project)