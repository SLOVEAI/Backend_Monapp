from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(models.Model):

    class Meta:
        app_label = 'user'

    class AccountType(models.TextChoices):
        Artist = 'Artist'
        Venue = 'Venue'
        Consumer = 'Consumer'

    firstname = models.CharField(max_length=120, null=True)
    lastname = models.CharField(max_length=120, null=True)
    email = models.CharField(max_length=120, unique=True, null=True)
    password = models.CharField(max_length=120)
    account_type = models.CharField(
        max_length=120, null=True, choices=AccountType.choices)
    brand_name = models.CharField(
        max_length=120,
        null=True
    )
    address = models.CharField(
        max_length=120,
        null=True
    )
    city = models.CharField(
        max_length=120,
        null=True
    )
    mobile_number = models.CharField(
        max_length=120,
        null=True
    )

    account_types_all = ArrayField(models.CharField(
        max_length=50, null=True), default=list)

    music_genres_all = ArrayField(models.CharField(
        max_length=120, null=True), default=list)

    profile_picture = models.CharField(
        max_length=1024,
        null=True
    )

    website_link = models.CharField(
        max_length=120,
        null=True
    )

    social_media_link = models.CharField(
        max_length=120,
        null=True
    )

    spotify_link = models.CharField(
        max_length=120,
        null=True
    )

    organization_name = models.CharField(
        max_length=120,
        null=True
    )

    venue_name = models.CharField(
        max_length=120,
        null=True
    )
    
    venue_type_all = ArrayField(models.CharField(
        max_length=120, null=True), default=list)

    venue_capacity = models.CharField(
        max_length=120,
        null=True
    )

    live_performance_per_month = models.CharField(
        max_length=120,
        null=True
    )

    preferred_genre = models.CharField(
        max_length=120,
        null=True
    )

    average_musician_exposure = models.CharField(
        max_length=120,
        null=True
    )

    social_media_followers = models.CharField(
        max_length=120,
        null=True
    )

    price_per_gig = models.CharField(
        max_length=120,
        null=True
    )

    specific_user_rating = models.CharField(
        max_length=120,
        null=True
    )

    peak_season = models.CharField(
        max_length=120,
        null=True
    )

    @property
    def fullname(self):
        return self.firstname + " " + self.lastname
