from photos import models
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('name',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ('comment', 'user')


class PhotoSerializer(serializers.ModelSerializer):
    tag_set = TagSerializer(many=True)
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = models.Photo
        fields = ('image', 'description', 'counter', 'tag_set', 'comment_set')
