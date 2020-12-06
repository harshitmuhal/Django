from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


# Article-Author : Many - to - one relationship
# Introduce a Foreign key in Many side. Foreign key is record of Author table
class Article(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=1000)
    author=models.ForeignKey('Author', on_delete = models.CASCADE)
    #on_delete specifies what to do to records of article when author is deleted from Author table
    #but that author is present in Article as FK
    #cascade deletion in DBMS is deleting all records if all FK records present in its main table
    #are deleted

    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=50)
    designation = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

# Many - to - Many relationship
#You can add pizza=models.ManyToManyField('Pizza ') in toppings as well

#If you use .tables command in sqlite then you will see an extra table for many to Many
#which records all the entries for Topping and pizza

class Topping(models.Model):
  name = models.CharField(max_length = 256)

  def __str__(self):
    return self.name

class Pizza(models.Model):
  name = models.CharField(max_length = 256)
  price = models.IntegerField(validators=[
    MinValueValidator(0)
  ])
  toppings = models.ManyToManyField('Topping')

  def __str__(self):
    return self.name


# Making our custom Many to Many relationship by making seperate table for the relationship ourselves
class Person(models.Model):
  name = models.CharField(max_length = 256)
  societies = models.ManyToManyField('Society', through = 'Membership')
  def __str__(self): return self.name

class Society(models.Model):
  name = models.CharField(max_length = 256)
  def __str__(self): return self.name

class Membership(models.Model):
  person_id = models.ForeignKey('Person', on_delete = models.CASCADE)
  society_id = models.ForeignKey('Society', on_delete = models.CASCADE)

  desgination = models.CharField(max_length = 256)
