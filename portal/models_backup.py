from django.db import models
from django.utils import timezone


class Robot(models.Model):

    controler = models.ForeignKey('auth.User')
    robot = models.CharField(max_length=200)
    motorspeedright = models.FloatField(blank=True)
    motorspeedleft = models.FloatField(blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)



    def publish(self):
        self.save()

    def __str__(self):
        return self.robot
