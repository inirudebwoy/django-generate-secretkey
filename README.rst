# django-generate-secretkey
Generates Django SECRET_KEY with management command and adds to settings.

Very composable in deployment scripts or other automation.

python manage.py generate_key -s >> settings.py
python manage.py generate_key settings.py
