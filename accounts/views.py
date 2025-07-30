from dj_rest_auth.views import LogoutView
from django.http import JsonResponse

class CustomLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.delete_cookie('sessionid')
        response.delete_cookie('csrftoken')
        return response
