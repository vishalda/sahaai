from django.db import models
from django.db.models.aggregates import Max
from ngo.models import Organization
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Event(models.Model):
    location=models.TextField()
    venue=models.TextField()
    ngo_id=models.ForeignKey(Organization,on_delete=models.CASCADE,default=None)
    name=models.CharField(max_length=100)
    cred_points=models.IntegerField(validators=[MaxValueValidator(20),MinValueValidator(1)])
    description=models.TextField()

    def __str__(self):
        return self.name