from django.db import models

class Activity_periods(models.Model):
    intime = models.TimeField(max_length=20)
    out_time = models.TimeField(max_length=20)