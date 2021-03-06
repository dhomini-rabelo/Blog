from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('posts.urls')),
    path('', include('categories.urls')),
    path('', include('accounts.urls')),
    path('', include('authors.urls')),
    path('summernote/', include('django_summernote.urls')),
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if False: 
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
