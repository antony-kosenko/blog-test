import uuid
from django_resized import ResizedImageField

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.files.storage import get_storage_class
from django.db import models

from accounts.managers import CustomUserManager
from accounts.services import CustomUserServices


class OverwriteStorage(get_storage_class()):
    """ Overwrites an existing file if file provided in request has a same name. """
    def _save(self, name, content):
        self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name, max_length=None):
        return name


def profile_avatar_path(instance, filename):
    # uploading avatar to dynamic PATH
    extension = filename.split(".")[-1]
    return f"accounts/{instance.username}/profile_image/{instance.username}_avatar.{extension}"


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom User model extends a pre-defined django AbstractUser model."""

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    username = models.CharField(max_length=64, unique=True)
    avatar = ResizedImageField(
        force_format="WEBP",
        crop=["middle", "center"],
        upload_to=profile_avatar_path,
        blank=True,
        null=True,
        max_length=500,
        storage=OverwriteStorage()
    )
    homepage = models.URLField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(verbose_name="staff status", default=False)
    is_active = models.BooleanField(verbose_name="active", default=True)
    date_created = models.DateTimeField(
        verbose_name="date joined",
        auto_now_add=True,
        blank=True,
        null=True
    )

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.username}[{self.email}]"

    def save(self, *args, **kwargs):
        if not self._password:
            password = CustomUserServices.generate_password()
            self.set_password(password)
        super(CustomUser, self).save(*args, **kwargs)
