from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage
from .models import Member


@receiver(post_delete, sender=Member)
def remove_profile_image(sender, instance, **kwargs):
    if instance.photo:
        try:
            default_storage.delete(instance.photo.path)
        except Exception as e:
            print(f'Error deleting profile image:\n{e}')
