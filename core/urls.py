from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from core.settings import base
from .settings import swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/', include('apps.mentors.urls')),
    path('api/v1/', include('apps.others.urls'))
]

urlpatterns += swagger.urlpatterns
urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
urlpatterns += static(base.STATIC_URL)