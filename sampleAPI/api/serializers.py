from rest_framework import serializers
from api import models


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    rollno = serializers.IntegerField()


# class ArticleSerializer(serializers.ModelSerializer):
#     class meta:
#         model=models.Article
#         fields='__all__'
