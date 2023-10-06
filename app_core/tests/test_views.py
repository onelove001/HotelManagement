from django.test import TestCase, Client
from django.urls import reverse
from app_core.models import *
from app_core.user_views import *


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
    
    def test_user_dashboard_GET(self):
        response = self.client.get(reverse("welcome-page"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")


    def test_about_GET(self):
        response = self.client.get(reverse("about"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")


    def test_contact_GET(self):
        response = self.client.get(reverse("contact"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")

    
    def test_login_GET(self):
        response = self.client.get(reverse("login-page"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")


    def test_admin_welcome_GET(self):
        response = self.client.get(reverse("admin-welcome-page"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "admin_templates/admin_home.html")


    def test_create_manager_GET(self):
        response = self.client.get(reverse("app:create-wing-manager"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "admin_templates/create_wing_manager.html")


    def test_create_suite_GET(self):
        response = self.client.get(reverse("app:create-suite"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "admin_templates/create_suite.html")


    

