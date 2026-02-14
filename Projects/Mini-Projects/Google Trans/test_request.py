import os
import django
from django.test import Client

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "google_translator.settings")
django.setup()

c = Client()
try:
    response = c.get('/')
    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        print(response.content.decode('utf-8'))
except Exception as e:
    print(f"Request failed: {e}")
