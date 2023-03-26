from faker import Faker
from Demo_App.models import Student

fake=Faker()
print(fake.sentence())

stud_list=Student.objects.all()
print(stud_list)

 