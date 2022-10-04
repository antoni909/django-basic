import os 

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

# Fake pop script

import random
from AppTwo.models import WebPage, Topic, Page, User
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace','News','Games']

def add_topic():

    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    print("POPULATING PAGES")
    for entry in range(N):
        #get topic for the entry
        top = add_topic()
        # create fake url object
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        # create new webpage entry
        webpg = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

def add_user(f,l,e):
    u = User.objects.get_or_create(firstN=f,lastN=l,email=e)[0]
    u.save()

def populateUsers(N=5):
    print("POPULATING USERS")
    for entry in range(N):
        fake = fakegen.name().split()
        first = fake[0]
        last = fake[1]
        email = fakegen.email()
        add_user(first,last,email)


if __name__ == '__main__':
    print('POPULATING DB')
    populate(20)
    populateUsers(20)
    print('POPULATING COMPLETE')
