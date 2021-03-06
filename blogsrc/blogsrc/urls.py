from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include, re_path

from articles.views import AboutTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/about/', AboutTemplate.as_view(), name="about"),
    path('', include('articles.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
