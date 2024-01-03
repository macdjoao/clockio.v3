from django.db import models
from django.contrib.auth.models import User


class Clock(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_clocks')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='updated_clocks', null=True)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    class Meta:
        ordering = ['-id']
        verbose_name = 'Clock'
        verbose_name_plural = 'Clocks'

    def __str__(self):
        return f'{self.created_by.username} - {self.check_in} - {self.check_out}'
