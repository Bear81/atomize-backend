from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Root route for sanity check
@api_view()
def root_route(request):
    return Response({"message": "Welcome to Atomize API 🚀"})

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('habits.urls')),

]

