from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
# Create your models here.

class MyUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):

        if not email:
            raise ValueError('Sähköposti on annettava')

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        if not email:
            raise ValueError('Sähköposti on annettava')

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Custom user model. Inherit PermissionsMixin
class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    group = models.ManyToManyField(Group, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name + "_" + self.last_name

    '''
    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    '''