from rest_framework import serializers
from .models import *
class StateLimitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = [
            'title',
            'short_description',
            'contact_number',
            'facebook_link',
            'instagram_link',
            'Image',
            'image_alt'
        ]

class StateFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CitiesLimitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = [
            'title',
            'short_description',
            'contact_number',
            'facebook_link',
            'instagram_link',
            'Image',
            'image_alt'
        ]

class CitiesFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'

