from django.dispatch import receiver
from django.db.models.signals import pre_save
from ..models import Customer,User
import logging

'''

@receiver(pre_save, sender=Customer)
def create_customer(sender, instance, **kwargs):
    if not instance.user:  # Check if the Customer instance doesn't have an associated User
        logging.debug("Creating a new user for the customer.")
        try:
            user = User.objects.create_user(
                email=instance.email,
                phone=instance.phone,
                first_name=instance.first_name,
                last_name=instance.last_name,
                password=instance.password
            )
            logging.debug(user)
            instance.user = user  # Assign the newly created User to the Customer
            logging.info(f'User created for customer: {instance.email}')
        except Exception as e:
            logging.error(f'Error creating user for customer: {e}')

@receiver(pre_save, sender=Customer)
def create_user_for_customer(sender, instance, **kwargs):
    
    
    if instance.pk is None:  # Check if this is a new instance
        if not hasattr(instance, 'user') or instance.user is None:
            # Create a User instance
            
            user = User.objects.create(
                email=instance.user.email,  # Ensure you have these fields on the Customer model or adjust accordingly
                phone=instance.phone,
                first_name=instance.first_name,
                last_name=instance.last_name,
                password=instance.password  # Make sure to handle password hashing
            )
            instance.user = user
            logging.debug("User created and linked to customer.")

            '''