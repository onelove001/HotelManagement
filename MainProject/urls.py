
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from app_core.views import *
from app_core.admin_views import *


urlpatterns = [

    path("admin/", admin.site.urls),
    path("", welcome_page, name="welcome-page"),
    path("admin_home", admin_home, name="admin-welcome-page"),
    path("login", login_page, name="login-page"),
    path("login_user", login_user, name="login-user"),
    path("logout_user", logout_page, name="logout-user"),
    path("register", register_page, name="register-user"),
    path("contact", contact, name="contact"),
    path("faq", faqq, name="faq"),
    path("about", about, name="about"),
    path("app/", include("app_core.urls", namespace="app")),

]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)