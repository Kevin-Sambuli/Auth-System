from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

# Activate the following when using React build templates and change the templates directory in the settings templates
# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
