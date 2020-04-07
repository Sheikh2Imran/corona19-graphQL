from datetime import datetime

from django.db import models


class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "District: {}".format(self.name)


class SubmittedCoronaCaseManager(models.Manager):
    def update_status_success(self, id):
        try:
            self.objects.filter(id=id).update(status='1')
        except Exception as e:
            print(e)
            return False

    def update_status_cancel(self, id):
        try:
            self.objects.filter(id=id).update(status='0')
        except Exception as e:
            print(e)
            return False


class SubmittedCoronaCase(models.Model):
    STATUS = (
        ('2', 'Pending'),
        ('1', 'Success'),
        ('0', 'Cancel'),
    )

    person_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=254)
    fb_link = models.CharField(max_length=265, null=False, blank=False)
    total_corona_case = models.IntegerField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    source = models.CharField(max_length=500, null=False, blank=False)
    status = models.CharField(max_length=1, choices=STATUS, default='2')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    objects = SubmittedCoronaCaseManager()

    def __str__(self):
        return "Submitted by: {} | Total corona case: {}".format(self.person_name, self.total_corona_case)


class CoronaCaseManager(models.Manager):
    def get_total_affected(self, today=None):
        if today:
            return self.objects.filter(updated_at=datetime.now).aggregate(Sum('affected'))
        return self.objects.aggregate(Sum('affected'))

    def get_death_affected(self, today=None):
        if today:
            return self.objects.filter(updated_at=datetime.now).aggregate(Sum('death'))
        return self.objects.aggregate(Sum('death'))

    def get_recovered_affected(self, today=None):
        if today:
            return self.objects.filter(updated_at=datetime.now).aggregate(Sum('recovered'))
        return self.objects.aggregate(Sum('recovered'))


class CoronaCase(models.Model):
    affected = models.IntegerField()
    death = models.IntegerField()
    recovered = models.IntegerField()
    district = models.CharField(max_length=1, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    objects = CoronaCaseManager()

    def __str__(self):
        return "Affected from: {}".format(self.district)

