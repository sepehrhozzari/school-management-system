"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.views import PasswordResetConfirmView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="School Management System",
        default_version="v1",
        description="APIs for School Management System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # urls for rest-auth third-party package
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # urls for account app
    path('api/v1/account/', include("account.urls", namespace="account_v1")),
    path('api/v2/account/', include("account.urls", namespace="account_v2")),

    # urls for exam app
    path('api/v1/exam/', include("exam.urls", namespace="exam_v1")),
    path('api/v2/exam/', include("exam.urls", namespace="exam_v2")),

    # urls for book app
    path('api/v1/book/', include("book.urls", namespace="book_v1")),
    path('api/v2/book/', include("book.urls", namespace="book_v2")),

    path('swagger/', schema_view.with_ui("swagger",
         cache_timeout=0), name="schema-swagger-ui"),
    path('redoc/', schema_view.with_ui("redoc",
         cache_timeout=0), name="schema-redoc"),
]
