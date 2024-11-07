from django.contrib import admin
from django.urls import path, include, re_path, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("groom/", include("groom.urls")),

]   

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)