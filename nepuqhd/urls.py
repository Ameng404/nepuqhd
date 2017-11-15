from django.conf.urls import url,include
from django.contrib import admin
from DjangoUeditor import urls as DjangoUeditor_urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'', include('nepuapp.urls',namespace='nepuapp', app_name='nepuapp')),
]

from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)