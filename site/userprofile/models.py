from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # email
    email = models.CharField(max_length=20, blank=True)
    # icon
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)
    def __str__(self):
        return 'user {}'.format(self.user.username)


# # 信号接收函数，每当新建 User 实例时自动调用
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# # 信号接收函数，每当更新 User 实例时自动调用
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
