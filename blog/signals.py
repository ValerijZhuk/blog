from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Post, Comment


def edit_signal(sender, instance, **kwargs):
    print('Called')
    for comments in instance.comments.all():
        if comments.rating < 3:
            comments.delete()


post_save.connect(edit_signal, sender=Post)


@receiver(post_save, sender=Comment)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print('Комментарий создан!')
