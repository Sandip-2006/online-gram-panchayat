from django.contrib import admin
from .models import complain

@admin.register(complain)
class complainview(admin.ModelAdmin):
    list_display = ('fname', 'phone_num', 'Email', 'complain','photo', 'Complaint_Details', 'created_at', 'updated_at')
