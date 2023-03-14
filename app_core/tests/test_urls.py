from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app_core.views import *
from app_core.student_views import *



class TestUrls(SimpleTestCase):

    def test_student_dashboard_is_resolved(self):

        url = reverse("app:student-dashboard")
        path = (resolve(url))
        self.assertEquals(path.func, student_dashboard)


    def test_guest_stay_is_resolved(self):

        url = reverse("app:guest-stay")
        path = (resolve(url))
        self.assertEquals(path.func, guest_stay)


    def test_payment_is_resolved(self):
        
        url = reverse("app:payment")
        path = (resolve(url))
        self.assertEquals(path.func, payment)

    
    def test_room_transfer_is_resolved(self):
        
        url = reverse("app:room-transfer")
        path = (resolve(url))
        self.assertEquals(path.func, room_transfer)


    def test_complain_is_resolved(self):
        
        url = reverse("app:complaints")
        path = (resolve(url))
        self.assertEquals(path.func, complaints)


    def test_login_is_resolved(self):
        
        url = reverse("login-page")
        path = (resolve(url))
        self.assertEquals(path.func, login_page)


    def test_welcome_page_is_resolved(self):
        
        url = reverse("welcome-page")
        path = (resolve(url))
        self.assertEquals(path.func, welcome_page)
