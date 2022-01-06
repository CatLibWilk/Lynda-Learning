from django.db import models

# Create your models here.
class Form(models.Model):
    study_name = models.CharField(max_length=200)
    primary_investigator = models.CharField(max_length=200)
    submit_date = models.DateTimeField('date published')