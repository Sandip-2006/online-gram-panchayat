from django.contrib import admin
from .models import Celebrity, Development, Gallery, Infrastructure, complain,Contact,Event

@admin.register(complain)
class complainAdmin(admin.ModelAdmin):
    list_display = ('fname', 'phone_num', 'Email', 'complain','photo', 'Complaint_Details', 'created_at', 'updated_at')

@admin.register(Contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','created_at']

@admin.register(Event)
class eventAdmin(admin.ModelAdmin):
    list_display = ['title','location','date']
    list_filter = ['date']
    search_fields = ['title', 'description']
    list_per_page = 10

@admin.register(Celebrity)
class celebrityAdmin(admin.ModelAdmin):
    list_display = ['name','created_at']

@admin.register(Gallery)
class galleryAdmin(admin.ModelAdmin):
    list_display = ['title','created_at']

@admin.register(Development)
class developmentAdmin(admin.ModelAdmin):
    list_display = ['title','short_description','created_at']
    list_filter = ['created_at']

    def short_description(self, obj):
        if len(obj.description) > 30:
            return obj.description[:30] + '...'
        return obj.description

    short_description.short_description = 'Description Preview'

@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']
    list_per_page = 10

    # Custom method to show only first 30 characters of description
    def short_description(self, obj):
        if len(obj.description) > 30:
            return obj.description[:30] + '...'
        return obj.description

    short_description.short_description = 'Description Preview'