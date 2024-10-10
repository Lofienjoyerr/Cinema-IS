import os
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from PIL import Image


def user_directory_path(instance, filename):
    path = 'userapp/user_{0}/avatar.{1}'.format(instance.id, filename.split('.')[-1])
    if instance.id is None:
        path = 'userapp/user_{0}/avatar.{1}'.format(User.objects.latest('id').id + 1, filename.split('.')[-1])
    if not instance.id is None:
        old_path = instance.avatar.path.replace('\\', '/').split('/')
        old_path = "/".join(old_path[:-1])
        if os.path.exists(old_path + '/' + path):
            os.remove(old_path + '/' + path)
    return path


class User(AbstractUser):
    date_joined = None
    last_login = None
    first_name = None
    last_name = None
    phone = models.CharField(max_length=12, unique=True)
    email = models.CharField(max_length=40, unique=True)
    avatar = models.ImageField(upload_to=user_directory_path,
                               default='userapp/default_avatar.webp',
                               validators=[FileExtensionValidator(['webp'])])

    def update_avatar(self):
        if not self.avatar == f"userapp/user_{self.id}/default_avatar.webp":
            img = Image.open(self.avatar.path)
            img.thumbnail((220, 220))
            img.save(self.avatar.path.split('.')[0] + '.webp', 'WEBP')
            img.close()
            if img.format == 'PNG' or img.format == 'JPG' or img.format == 'JPEG':
                os.remove(self.avatar.path)
                self.avatar = 'userapp/user_{0}/avatar.{1}'.format(self.id, 'webp')
                self.save()

    def create_user(self, **kwargs):
        self.__dict__.update(kwargs)
        self.set_password(kwargs.get('password'))
        self.save()
