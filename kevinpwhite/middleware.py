from django.http import HttpResponse
from django.conf import settings

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.MAINTENANCE_MODE == "on":
            return HttpResponse(
                "<h1>Site Under Maintenance</h1><p>We will be back soon.</p>",
                status=503
            )
        return self.get_response(request)
