from django.db import models
from django.contrib.auth.models import User


class Clock(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_clocks')

    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='updated_clocks')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    check_in_date = models.DateField()
    check_out_date = models.DateField()

    check_in_hour = models.TimeField()
    check_out_hour = models.TimeField()

    class Meta:
        ordering = ['-id']
        verbose_name = "Clock"
        verbose_name_plural = "Clocks"

    def __str__(self):
        return f"{self.user.username} - {self.check_in_date}/{self.check_in_hour.strftime('%H:%M')} - {self.check_out_date}/{self.check_out_hour.strftime('%H:%M')}"
