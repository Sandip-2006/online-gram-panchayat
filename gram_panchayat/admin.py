from django.contrib import admin
from .models import Celebrity, Development, Document, Gallery, GramSabhaMeeting, Infrastructure, Scheme, complain,Contact,Event,staffs,members,Sarpanch

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

@admin.register(Sarpanch)
class SarpanchAdmin(admin.ModelAdmin):
    list_display = ['sarpanch_name','start_year','end_year']
    
@admin.register(Scheme)
class SchemeAdmin(admin.ModelAdmin):
    list_display = ['scheme_name','short_about','created_at']
    list_filter = ['scheme_name']
    search_fields = ['scheme_name']
    list_per_page = 10
    ordering = ['scheme_name']

    def short_about(self,obj):
        if len(obj.about) > 30:
            return obj.about[:30] + '...'
        return obj.about
    
    short_about.short_description = "About"  # column heading

@admin.register(GramSabhaMeeting)
class GramSabhaMeetingAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "time", "venue", "is_upcoming")
    search_fields = ("title", "agenda", "venue")
    list_filter = ("date",)
    ordering = ("-date",)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
