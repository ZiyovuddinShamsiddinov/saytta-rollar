from django.contrib.auth.models import BaseUserManager

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

class BaseModel(models.Model):
    created_ed=models.DateTimeField(auto_now_add=True)
    updated_ed=models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract=True


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, email=None, **extra_fields):
        """Oddiy foydalanuvchi yaratish uchun"""
        if not phone_number:
            raise ValueError("phone_number maydoni majburiy")

        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, email=None, **extra_fields):
        """Superuser yaratish uchun"""
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser is_admin=True bo‘lishi kerak')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser is_staff=True bo‘lishi kerak')

        return self.create_user(phone_number, password, email, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '998900404001'. Up to 14 digits allowed.")

    phone_number = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Foydalanuvchini bloklash uchun

    objects = CustomUserManager()  # Custom manager qo‘shamiz

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.phone_number

    @property
    def is_superuser(self):
        return self.is_admin

class Teacher(BaseModel):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name=models.CharField(max_length=150)
    phone=models.CharField(max_length=15)
    location=models.CharField(max_length=255)
    teacher=models.ForeignKey(Teacher , on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name