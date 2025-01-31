from django.core.management.base import BaseCommand
from user_auth.models import UserType, User
import random

class Command(BaseCommand):
    help = 'Seed the database with default data'

    def handle(self, *args, **kwargs):
        # Create default user types
        user_types = ['Admin', 'Institution Representative', 'Instructor', 'Student']
        for user_type in user_types:
            UserType.objects.get_or_create(name=user_type)

        # Create a default admin user
        admin_type = UserType.objects.get(name='Admin')
        if not User.objects.filter(email='admin@example.com').exists():
            User.objects.create(
                user_id=random.randint(10000, 99999),
                user_type=admin_type,
                first_name='Default',
                last_name='Admin',
                email='admin@example.com',
                password='admin'  # Password will be hashed
            )
            self.stdout.write(self.style.SUCCESS('Default admin user created.'))
        else:
            self.stdout.write(self.style.WARNING('Default admin user already exists.'))