from django.forms import model_to_dict
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from sport.models import Sport


# class SportSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     slug = serializers.SlugField(read_only=True)
#     photo = serializers.ImageField(default=None)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Sport.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.slug = validated_data.get('slug', instance.slug)
#         instance.photo = validated_data.get('photo', instance.photo)
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         return instance

class SportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sport
        fields = ('__all__')
        read_only_fields = ('slug', 'time_create', 'time_update')