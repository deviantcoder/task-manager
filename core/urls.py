from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.shortcuts import redirect


def root_redirect(request):
    return redirect('tasks:project_list')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_redirect),
    path('', include('apps.accounts.urls')),
    path('', include('apps.tasks.urls')),
]

if getattr(settings, 'DEBUG', False):
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns += debug_toolbar_urls()
