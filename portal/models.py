from django.db import models
from django.utils import timezone


class Robot(models.Model):

    controler = models.ForeignKey('auth.User')
    robot = models.CharField(max_length=200)
    task_number = models.FloatField(blank=True)
    task_time = models.FloatField(blank=True)
    task_speed = models.FloatField(blank=True)
    task_direction = models.CharField(max_length=200)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.robot
