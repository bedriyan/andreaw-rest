from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('rest_api.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

# you can directly write all urls here but using include('andrew_rest.url') keeps it clear.