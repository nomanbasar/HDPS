from django.db import models

# Create your models here.


class DiseasesModel(models.Model):
    age = models.CharField(max_length=100, blank=False, null=False)
    pain_type = models.CharField(max_length=100, blank=False, null=False)
    blood_pressure = models.CharField(max_length=100, blank=False, null=False)
    cholesterol = models.CharField(max_length=100, blank=False, null=False)
    blood_sugar = models.CharField(max_length=100, blank=False, null=False)
    ecg = models.CharField(max_length=100, blank=False, null=False)
    hart_rate = models.CharField(max_length=100, blank=False, null=False)
    exang = models.CharField(max_length=100, blank=False, null=False)
    old_peak = models.CharField(max_length=100, blank=False, null=False)
    slope = models.CharField(max_length=100, blank=False, null=False)
    ca = models.CharField(max_length=100, blank=False, null=False)
    thal = models.CharField(max_length=100, blank=False, null=False)
    male = models.BooleanField(default=False)
    female = models.BooleanField(default=False)
