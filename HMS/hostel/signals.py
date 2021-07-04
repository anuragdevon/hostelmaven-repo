from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminDean.objects.create(admin=instance)
        elif instance.user_type == 2:
            Staff.objects.create(admin=instance)
        elif instance.user_type == 3:
            Student.objects.create(admin=instance, session_year_id=Session.objects.get(id=1))

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.Dean.save()
    elif instance.user_type == 2:
        instance.Staff.save()
    elif instance.user_type == 3:
        instance.Student.save()
