from django.contrib import admin
from .models import Celebrity, Gallery, complain,Contact,Event

@admin.register(complain)
class complainview(admin.ModelAdmin):
    list_display = ('fname', 'phone_num', 'Email', 'complain','photo', 'Complaint_Details', 'created_at', 'updated_at')

@admin.register(Contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','created_at']

@admin.register(Event)
class eventAdmin(admin.ModelAdmin):
    list_display = ['title','location','date']

@admin.register(Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    list_display = ['name','created_at']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title','created_at']