from django.db import models
from rest_framework import fields, viewsets, serializers
from django.contrib.auth.hashers import make_password

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['id',  'email', 'password',
                  'account_type', 'account_types_all',
                  'mobile_number', 'city', 'address',
                  'brand_name', 'profile_picture', 'music_genres_all',
                  'profile_picture', 'website_link',
                  'social_media_link', 'spotify_link',
                  'organization_name','venue_name', 'venue_type_all', 'venue_capacity',
                  'live_performance_per_month', 'preferred_genre', 'average_musician_exposure',
                  'social_media_followers', 'price_per_gig','specific_user_rating',
                  'peak_season']

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
