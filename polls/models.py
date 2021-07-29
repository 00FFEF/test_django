from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    public_data = models.CharField(max_length=100)
    votes = models.DecimalField(max_digits=20, decimal_places=10)

class Economics(models.Model):
    title = models.CharField(max_length=100)
    href = models.CharField(max_length=100)
    create_data = models.CharField(max_length=100)
