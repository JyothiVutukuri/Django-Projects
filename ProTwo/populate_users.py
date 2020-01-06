import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django
django.setup()

import random
from app_two.models import User
from faker import Faker

fake_gen = Faker()


def populate(N=5):

    for each in range(N):
        f_name = fake_gen.name()
        f_fname = f_name[0]
        f_lname = f_name[1]
        f_email = fake_gen.email()

        user = User.objects.get_or_create(first_name=f_fname, last_name=f_lname, email=f_email)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')



