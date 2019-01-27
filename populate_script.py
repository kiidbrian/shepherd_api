import os, django, random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shepherd_api.settings")
django.setup()

from faker import Faker
from faker.providers import phone_number,internet
from api.models import User,Member,Attendance
from django.utils import timezone

fake = Faker()
fake.add_provider(phone_number)
fake.add_provider(internet)

def create_users(N):
    """
    A Method to populate test User data
    """
    for _ in range(N):
        name = fake.name()
        phone = fake.phone_number()
        email = fake.email()
        role = random.choice(["shepherd","admin"])
        password = fake.user_name
        User.objects.create(
            name=name,phone=phone,
            email=email,role=role,
            password=password
        )

def create_members(N):
    """
    A method to populate test Members data
    """
    for _ in range(N):
        name = fake.name()
        phone = fake.phone_number()
        email = fake.email()
        address = fake.address()
        Member.objects.create(
            name=name,phone=phone,
            email=email,address=address
        )


# create_users(20)
create_members(20)
print(" ==> Models successfully populated :)")