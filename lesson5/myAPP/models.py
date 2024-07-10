from django.db import models

# Create your models here.

STUDENT_ROLE = (
    ("ENROLLED","enrolled"),
    ("INQUIRED","inquired"),
    ("COMPLETED","completed")

)    


class Student (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.BooleanField(default=True)
    role = models.CharField(max_length=100, choices= STUDENT_ROLE,default="INQUIRED")


