"""
URL configuration for the_phantom_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from finance_app import views as finance_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic import RedirectView

handler404 = 'bi_app.views.error_404' 
handler500 = 'bi_app.views.error_500'

descope_admin_site = admin.site
# override the login template with our own
descope_admin_site.login_template = "admin_login.html"


urlpatterns = [
    path("", include("bi_app.urls")),
    path('finance_app/', include('finance_app.urls')),
    path('land_app/', include('land_app.urls')),
    path('api/', include('API.urls')),
    path('authentication/', include('authentication.urls')),
    path('admin/', descope_admin_site.urls),
    path('auth/', include('django_descope.urls')),
    # path('auth/google/callback', land_views.google_callback, name='google_callback'),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
