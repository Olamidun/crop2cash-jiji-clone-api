"""jiji_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from drf_yasg import openapi
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view


# Swagger configurations
schema_view = get_schema_view(
   openapi.Info(
      title="C2C Jiji Clone API",
      default_version='v1',
      description="Documentation for C2C Jiji clone API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kolapoolamidun@gmail.com"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('sellers/', include('seller.urls')),
    path('items/', include('items.urls')),
    path('buyers/', include('buyers.urls'))
]

if settings.DEBUG:
    # Media files url and folder configurations
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


