from django.urls import path, include

# from django.conf.urls import include, url
# from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path("", include("ponycheckup.check.urls")),
]

# urlpatterns = [
#     "",
#     # Examples:
#     # url(r'^$', 'ponycheckup.views.home', name='home'),
#     url(r"^", include("ponycheckup.check.urls", namespace="check")),
#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# ]
# if settings.dev.DEBUG:
import debug_toolbar

urlpatterns = [path("__debug__/", include(debug_toolbar.urls)),] + urlpatterns
