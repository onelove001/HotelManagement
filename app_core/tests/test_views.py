from django.test import TestCase, Client
from django.urls import reverse
from app_core.models import *


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
    
    def test_student_dashboard_GET(self):
        response = self.client.get(reverse("welcome-page"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")


    def test_student_page_GET(self):
        response = self.client.get(reverse("view-rooms"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "view_rooms.html")

    
    def test_login_GET(self):
        response = self.client.get(reverse("login-page"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")


    def test_admin_welcome_GET(self):
        response = self.client.get(reverse("admin-welcome-page"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "admin_templates/admin_home.html")


    def test_create_manager_GET(self):
        response = self.client.get(reverse("app:create-manager"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "admin_templates/create_manager.html")


    

