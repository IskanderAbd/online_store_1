from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from online_store_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/category/', include('applications.category.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
