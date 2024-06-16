# populate_db.py

import os
import django

def setup_django():
    # Set up Django's environment
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    django.setup()

def create_people():
    # Import your model
    from sim.models import Person
    # Import the people_data
    from data.people import people_data

    # Delete all existing entries
    Person.objects.all().delete()
    print("Deleted all existing Person entries.")

    # Create the data
    for name, description in people_data:
        person = Person.objects.create(name=name, description=description)
        print('🧑 Created', person.name)

if __name__ == "__main__":
    setup_django()
    create_people()
