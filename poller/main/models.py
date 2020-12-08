from django.db import models
from django.db import models
# Create your models here.
class question(models.Model):
    content=models.CharField(max_length=2000)

    def __str__(self):
        return self.content

class choice(models.Model):
    question=models.ForeignKey('question',on_delete=models.CASCADE)
    content=models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.question.content[:50], self.content)
