from django.db import models
from django.contrib.auth.models import User


class Band(models.Model):
    """
    Represents a musical band.

    :ivar name: The name of the band.
    :vartype name: str
    :ivar genre: The genre of music the band plays.
    :vartype genre: str
    :ivar origin: The place where the band originates.
    :vartype origin: str
    :ivar formation_date: The date when the band was formed.
    :vartype formation_date: date
    :ivar biography: A brief biography or description of the band.
    :vartype biography: str
    :ivar social_media_links: URLs to the band's social media profiles.
    :vartype social_media_links: str
    """

    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    origin = models.CharField(max_length=100)
    formation_date = models.DateField()
    biography = models.TextField()
    social_media_links = models.URLField()

    def __str__(self):
        """
        Returns the string representation of the band.

        :return: The name of the band.
        :rtype: str
        """
        return self.name


class Track(models.Model):
    """
    Represents a musical track.

    :ivar band: The band associated with the track.
    :vartype band: Band
    :ivar title: The title of the track.
    :vartype title: str
    :ivar duration: The duration of the track.
    :vartype duration: timedelta
    :ivar release_date: The date when the track was released.
    :vartype release_date: date
    :ivar audio_file: The file path to the audio file of the track.
    :vartype audio_file: str
    """

    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    release_date = models.DateField()
    audio_file = models.FileField(upload_to='music/')

    def __str__(self):
        """
        Returns the string representation of the track.

        :return: The title of the track.
        :rtype: str
        """
        return self.title


class UserProfile(models.Model):
    """
    Represents a user profile.

    :ivar user: The user associated with the profile.
    :vartype user: User
    :ivar favorite_tracks: The favorite tracks of the user.
    :vartype favorite_tracks: QuerySet
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_tracks = models.ManyToManyField(Track)

    def __str__(self):
        """
        Returns the string representation of the user profile.

        :return: The username of the user.
        :rtype: str
        """
        return self.user.username


class Review(models.Model):
    """
    Represents a review of a track by a user.

    :ivar user: The user who wrote the review.
    :vartype user: User
    :ivar track: The track being reviewed.
    :vartype track: Track
    :ivar rating: The rating given to the track (1 to 5).
    :vartype rating: int
    :ivar comment: The comment or review text.
    :vartype comment: str
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        """
        Returns the string representation of the review.

        :return: Username and title of the reviewed track.
        :rtype: str
        """
        return f"{self.user.username} - {self.track.title}"
