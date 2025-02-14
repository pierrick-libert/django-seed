"""
app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

# pylint: disable=invalid-name
urlpatterns = [
    path("admin/", admin.site.urls),
]

if settings.APP_NAME == "web":
    from .views import DashboardView, LoginView, LogoutView

    urlpatterns += i18n_patterns(
        path("login/", LoginView.as_view(), name="login"),
        path("logout/", LogoutView.as_view(), name="logout"),
        path("", DashboardView.as_view(), name="dashboard"),
        path("", include("user.urls", namespace="user")),
    )

elif settings.APP_NAME == "api":
    urlpatterns += [
        path("api/", include("api.urls")),
    ]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
