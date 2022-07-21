from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path , path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('', include('main.urls')),
    path('', include('gallery.urls')),
    path('payment/', include('payment.urls')),
    path('account/', include('account.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
