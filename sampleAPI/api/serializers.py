from rest_framework import serializers
from api import models


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    rollno = serializers.IntegerField()

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Tag
    fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many = True, read_only = True) #if you don;t serialise explicitly then in tags
    # you will see only primary keys. Check by removing this line.
    class Meta:
        model=models.Article
        fields='__all__'
