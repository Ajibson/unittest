from django.test import TestCase, Client
from django.urls import reverse, resolve

class TestRegistration(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    