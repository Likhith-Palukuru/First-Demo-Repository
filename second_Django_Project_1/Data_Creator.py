from faker import Faker
from Demo_App.models import Student

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_Django_Project.settings')
import django
django.setup()

fake=Faker()
serialno=4
for i in range(7):
    print(fake.name())
    print(fake.address())
    Std_rec=Student.objects.get_or_create(sno=serialno,sname=fake.name(),saddr=fake.address())
    serialno=serialno+1




