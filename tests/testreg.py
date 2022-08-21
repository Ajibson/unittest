from django.test import TestCase, Client
from django.urls import reverse, resolve
from account.views import register
import random
from account.models import User
class TestRegistration(TestCase):

    def setUp(self) -> None:
        self.reg_url = reverse("account:register")
        self.client = Client()

    def test_regurl_resolves(self):
        url = resolve(reverse("account:register"))
        self.assertEqual(url.func, register)

    
    def test_reg_urlresolves_with_405_for_get_reguest(self):
        response = self.client.get(self.reg_url)
        self.assertEqual(response.status_code, 405)

    def test_urlreg_with_no_data(self):
        response = self.client.post(self.reg_url, data={})

        for field in ["email", "password"]:
            self.assertIn("This field is required.", response.json()[field])
        self.assertEqual(response.status_code, 400)
    
    def test_urlreg_with_data(self) -> None:
        wrong_passwords = ["aze12", "1234747449494", "azeezybdjhddhdhd"]
        wrong_emails = ["a", "@mail.com"]
        for password in wrong_passwords:
            data = {"email": random.choice(wrong_emails), "password": password}
            response = self.client.post(self.reg_url, data=data)
            for key in ["email", "password"]:
                self.assertIn(key, response.json().keys())
        self.assertEqual(response.status_code, 400)

    def test_api_register_valid_data(self) -> None:
        data = {"email": "a@mail.com", "password": "azeez1233"}

        response = self.client.post(self.reg_url, data=data)
        db_users = User.objects.all()
        self.assertIn("success", response.json().keys())
        self.assertEqual(db_users.count(), 1)
        self.assertEqual(response.status_code, 200)
