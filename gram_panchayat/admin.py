from django.contrib import admin
from .models import Celebrity, Gallery, complain,Contact,Event,staffs,members

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

@admin.register(staffs)
class staffsAdmin(admin.ModelAdmin):
    list_display = ['staff_mem_name','staff_mem_position']
    list_filter = ['staff_mem_position']
    search_fields = ['staff_mem_name']
    list_per_page = 10
    ordering = ['staff_mem_name']
    list_editable = ['staff_mem_position']
    list_display_links = ['staff_mem_name']
    

@admin.register(members)
class membersAdmin(admin.ModelAdmin):
    list_display= ['member_name','member_position']
    list_filter = ['member_name']
    search_fields = ['member_name']
    list_per_page = 10
    ordering = ['member_name']
    list_editable = ['member_position']
    list_display_links = ['member_name']
