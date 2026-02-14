from django.conf import settings
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "google_translator.settings")
django.setup()

try:
    from translator import views
    print("Successfully imported views")
except Exception as e:
    print(f"Error importing views: {e}")
