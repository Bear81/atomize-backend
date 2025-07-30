# atomize_backend/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

@ensure_csrf_cookie
def csrf_debug(request):
    return JsonResponse({'message': 'CSRF cookie set'}, status=200)

@api_view()
def root_route(request):
    return Response({"message": "Welcome to Atomize API 🚀"})

urlpatterns = [
    path('csrf/', csrf_debug),  # ✅ This line is key
    path('', root_route),
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('habits.urls')),
]
