from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    ROLE_CHOICES = (
        ('EMPLOYER', 'Employer'),
        ('EMPLOYEE', 'Employee'),
    )

    role = models.CharField(max_length=8, choices=ROLE_CHOICES)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_profile')
    document = models.CharField(max_length=11)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.user.username} - {self.role} - {self.document}'

    @property
    def is_employer(self):
        return self.role == 'EMPLOYER'

    @property
    def is_employee(self):
        return self.role == 'EMPLOYEE'
