from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Online Gram Panchayat System"
admin.site.site_title = "Gram Panchayat Admin Portal"
admin.site.index_title = "Welcome to Admin Dashboard"


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('gram_panchayat.urls')),
    path("accounts/", include("django.contrib.auth.urls")),


    path("__reload__/", include("django_browser_reload.urls")),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


