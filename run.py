import os

# Iniciar proyecto Wagtail
os.system('wagtail start mycms')

# Cambiar directorio
os.chdir('mycms')

# Ejecutar migraciones
os.system('python manage.py migrate')

# Crear superusuario
os.system('python manage.py createsuperuser')

# Ejecutar servidor
os.system('python manage.py runserver')
