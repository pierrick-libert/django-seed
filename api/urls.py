"""Main URLs endpoints"""

from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import SimpleRouter


class OptionalSlashRouter(SimpleRouter):
    """OptionalSlashRouter"""

    def __init__(self):
        """Init"""
        super().__init__()
        self.trailing_slash = "/?"


urlpatterns = [
    path("", include("api.sample.urls")),
    # Swagger
    path(
        "swagger/",
        TemplateView.as_view(template_name="swagger/api.swagger.html", extra_context={"schema_url": "openapi-schema"}),
        name="swagger",
    ),
]
