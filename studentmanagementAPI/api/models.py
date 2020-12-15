from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Student(models.Model):
    GENDERS=[
        ('f','female'),
        ('m','male'),
        ('u','undisclosed'),
    ]
    name=models.CharField(max_length=256)
    rollno=models.IntegerField(unique=True,null=False,blank=False)
    email=models.EmailField()
    gender=models.CharField(max_length=1,choices=GENDERS)
    percentage=models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    institute = models.ForeignKey("Institute", on_delete = models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.name

class Institute(models.Model):
    TYPES = (
        ("h", "High School"),
        ("c", "College")
    )
    name = models.CharField(max_length = 200)
    type_of_institute = models.CharField(max_length = 1, choices = TYPES, null = True)

    def __str__(self):
        return self.name
