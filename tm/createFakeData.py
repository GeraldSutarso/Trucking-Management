import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tm.settings")

import django 
django.setup()
from faker import Faker
from faker_vehicle import VehicleProvider
from vehicles.models import *
from accounts.models import *
from model_bakery import baker
from model_bakery.recipe import Recipe, foreign_key

fake = Faker()
fake.add_provider(VehicleProvider)

# Create a recipe for User model with custom fields
user_recipe = Recipe(
    User,
    username = fake.user_name(),
    email = fake.free_email(),
    phone_number = fake.phone_number(),
    is_customer = fake.boolean(chance_of_getting_true=50),
    is_driver = fake.boolean(chance_of_getting_true=50),
    is_superuser = fake.boolean(chance_of_getting_true=10),
    is_staff = fake.boolean(chance_of_getting_true=0),
)

# Create a recipe for Customer model with custom fields
customer_recipe = Recipe(
    Customer,
    user = foreign_key(user_recipe),
    address = fake.address(),
)

# Create a recipe for Driver model with custom fields
driver_recipe = Recipe(
    Driver,
    user = foreign_key(user_recipe),
    license_number = fake.license_plate(),
    availability = fake.boolean(chance_of_getting_true=80),
    profile_picture = fake.image_url(),
    profile_picture_confirmed = fake.boolean(chance_of_getting_true=10),
    accepted = fake.boolean(chance_of_getting_true=5),
)

# Create a recipe for Admin model with custom fields
admin_recipe = Recipe(
    Admin,
    user = foreign_key(user_recipe),
)

# Create a recipe for Truck model with custom fields
truck_recipe = Recipe(
    Truck,
    model = fake.vehicle_make_model(),
    license_plate = fake.license_plate(),
    driver = foreign_key(driver_recipe),
    capacity = fake.random_int(min=1, max=10),
)

# Create a recipe for Maintenance model with custom fields
maintenance_recipe = Recipe(
    Maintenance,
    truck = foreign_key(truck_recipe),
    sensor_type = fake.random_element(elements=['temperature', 'pressure', 'humidity', 'vibration']),
    notification_date = fake.date_time_between(start_date='-1y', end_date='now'),
    status = fake.random_element(elements=['pending', 'in progress', 'completed', 'cancelled']),
)

# Generate fake data using the recipes
num_of_users = 100 # You can change this number as you wish
users = user_recipe.make(_quantity=num_of_users)
customers = customer_recipe.make(_quantity=num_of_users)
drivers = driver_recipe.make(_quantity=num_of_users)
admins = admin_recipe.make(_quantity=num_of_users)
trucks = truck_recipe.make(_quantity=num_of_users)
maintenances = maintenance_recipe.make(_quantity=num_of_users)