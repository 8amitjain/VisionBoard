from rest_framework import serializers
from .models import Vision, Photo


class VisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vision
        fields = ['user', 'title', 'content', 'image', 'image_height', 'image_width']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['file', 'vision']
