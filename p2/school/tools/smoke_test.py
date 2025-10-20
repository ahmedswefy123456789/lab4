"""Run quick smoke checks against the Django app using the test client.
This script must be run using the project virtualenv Python and from the project root.
"""
import os
import sys
import django
from django.conf import settings

# Ensure the project root (the folder that contains manage.py and the
# `school` package) is on sys.path so `import school` and
# DJANGO_SETTINGS_MODULE work when this script is run from any working
# directory. `tools/` is inside the project folder, so go one level up.
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(THIS_DIR, '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.test import Client

User = get_user_model()

# Ensure superuser exists
if not User.objects.filter(is_superuser=True).exists():
    print('Creating a default superuser: admin / admin')
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')

c = Client()

urls = ['/students/', '/courses/']
for u in urls:
    r = c.get(u)
    print(f'GET {u} -> {r.status_code}')

print('Smoke test finished')
