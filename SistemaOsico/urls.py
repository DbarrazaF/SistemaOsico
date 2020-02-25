
from django.contrib import admin
from django.urls import path, include
from principal import views as view_principal
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_principal.Index.as_view(), name='Index'),
    path('principal/', include('principal.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)