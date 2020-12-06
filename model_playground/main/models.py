from django.db import models
from django.db import models
from django.core.validators import (
  EmailValidator,
  MaxValueValidator,
  MinValueValidator,
  URLValidator,
  validate_slug   #It validates whether a string is a perfect slug or not
)
from main.validators import (
  validate_even_number
)

# Create your models here.

#each table is represented by a class
#each row is added using an object
class student(models.Model):
    # It is a practise to initialise constants with all capitals
    GENDERS=(
    ('f','Female'), #First entry is what will be stored in db and 2nd is what will user see
    ('m','Male'),
    ('u','Undisclosed')
    )

    #adding attributes
    name=models.CharField(max_length=100)

    roll_number=models.IntegerField(unique=True)

    address=models.TextField(null=True,blank=True)
    #By default fields are not null. If you want null specify it
    #null = True only means that field can be null in databases
    #but not null in ORM level
    #ORM layer converts python code to actual databases, tables etc.
    #so even if this is a null field you can't leave it empty while adding a row.
    # so we add blank=True for null at ORM level null as well

    phone_no=models.CharField(max_length=15,null=True)

    # email=models.EmailField(null=True)
    #EmailValidator is a class so we instantiate its object here
    email = models.CharField(max_length = 100, null = True, validators = [EmailValidator("Email address is not valid")])

    age = models.IntegerField(
    null = True,
    validators = [
      MaxValueValidator(150),
      MinValueValidator(0),
      validate_even_number
    ]
  )

    gender=models.CharField(max_length=1,choices=GENDERS,null=True)

    # Dunder functions to use name as name of each record of the tables
    def __str__(self):
        return self.name
