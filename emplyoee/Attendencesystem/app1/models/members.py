from django.db import models
from .activity_periods import Activity_periods

# <<<--------Inthis model we  used foreignkey for importing field of another model in this model----->
class Members(models.Model):
    employee = models.CharField(max_length=100)
    Real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=50)
    activity = models.ForeignKey(Activity_periods, on_delete= models.CASCADE,default=1, max_length=200)# ForeignKey used field

    def __str__(self):
        return self.Real_name


        