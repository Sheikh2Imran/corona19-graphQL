from django.utils import timezone
import datetime
from django.db import models


class SubmittedCoronaCase(models.Model):
    STATUS = (
        ('2', 'Pending'),
        ('1', 'Accept'),
        ('0', 'Cancel'),
    )
    person_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=254)
    fb_link = models.CharField(max_length=265, null=False, blank=False)
    affected = models.IntegerField(default=0)
    death = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    district = models.CharField(max_length=265, null=False, blank=False)
    source = models.CharField(max_length=500, null=False, blank=False)
    status = models.CharField(max_length=1, choices=STATUS, default='2')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Submitted by: {}".format(self.person_name)


class CoronaCase(models.Model):
    affected = models.IntegerField(default=0)
    death = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    district = models.CharField(max_length=265, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Affected from: {}".format(self.district)

