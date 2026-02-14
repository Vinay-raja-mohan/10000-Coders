import os
import django
from django.test import RequestFactory
# Setup Django environment BEFORE importing views
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "google_translator.settings")
django.setup()

from translator import views

factory = RequestFactory()
request = factory.get('/')

try:
    response = views.index(request)
    print(f"Status Code: {response.status_code}")
except Exception as e:
    import traceback
    traceback.print_exc()
