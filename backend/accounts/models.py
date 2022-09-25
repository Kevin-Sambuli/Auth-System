from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from rest_framework.authtoken.models import Token
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.conf import settings
from django.db import models
from .manager import UserManager


class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email = models.EmailField(verbose_name='Email', blank=False, max_length=100, unique=True)
    username = models.CharField('Username', max_length=30, unique=True)
    date_joined = models.DateTimeField('Date Joined', auto_now_add=True)

    # permissions
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField('admin', default=False)
    is_active = models.BooleanField('active', default=False)
    is_staff = models.BooleanField('staff', default=False)
    is_superuser = models.BooleanField('superuser', default=False)

    # unique parameter that will be used to login in the user
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    # hooking the New customized Manager to our Model
    objects = UserManager()

    class Meta:
        db_table = 'accounts'
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return '{}'.format(self.get_full_name())

    def get_full_name(self):
        """ Returns the first_name plus the last_name, with a space in between. """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    # For checking permissions. to keep it simple all admin have ALL permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

    def email_user(self, subject, message):
        """Sends an email to this User. """
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [self.email], fail_silently=False)


# class Profile(models.Model):
#     MALE = 'm'
#     FEMALE = 'f'
#     GENDER = [
#         (MALE, 'Male'),
#         (FEMALE, 'Female')
#     ]
#     owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Owner', blank=True,
#                                  null=True, default=None)
#     gender = models.CharField('Gender', max_length=5, choices=GENDER)
#     kra_pin = models.CharField('KRA PIN', max_length=20, unique=True, null=True, blank=False)
#     id_no = models.CharField('ID NO', max_length=10, unique=True, blank=False, null=True, )
#     dob = models.DateField('Date of Birth', blank=False, null=True)
#     phone_regex = RegexValidator(regex=r'^\d{10}$', message="phone number should exactly be in 10 digits")
#     phone = models.CharField('Contact Phone', max_length=255, validators=[phone_regex], unique=True, blank=True,
#                              null=True)  # you can set it unique = True
#     profile_image = models.ImageField("Profile Image", max_length=255, upload_to='profile_images', null=True,
#                                       blank=True)
#
#     class Meta:
#         db_table = 'profile'
#         verbose_name = "Profile"
#         verbose_name_plural = "User Profile"

    # def __str__(self):
    #     return '{}'.format(self.owner.username)


