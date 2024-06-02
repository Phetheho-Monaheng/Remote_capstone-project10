class Band(models.Model):
    """
    Represents a musical band.

    Attributes:
        name (str): The name of the band.
        genre (str): The genre of music the band plays.
        origin (str): The place where the band originates.
        formation_date (date): The date when the band was formed.
        biography (str): A brief biography or description of the band.
        social_media_links (str): URLs to the band's social media profiles.
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
        """
        return self.name

class Track(models.Model):
    """
    Represents a musical track.

    Attributes:
        band (Band): The band associated with the track.
        title (str): The title of the track.
        duration (timedelta): The duration of the track.
        release_date (date): The date when the track was released.
        audio_file (str): The file path to the audio file of the track.
    """

    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    release_date = models.DateField()
    audio_file = models.FileField(upload_to='music/')

    def __str__(self):
        """
        Returns the string representation of the track.
        """
        return self.title

class UserProfile(models.Model):
    """
    Represents a user profile.

    Attributes:
        user (User): The user associated with the profile.
        favorite_tracks (QuerySet): The favorite tracks of the user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_tracks = models.ManyToManyField(Track)

    def __str__(self):
        """
        Returns the string representation of the user profile.
        """
        return self.user.username

class Review(models.Model):
    """
    Represents a review of a track by a user.

    Attributes:
        user (User): The user who wrote the review.
        track (Track): The track being reviewed.
        rating (int): The rating given to the track (1 to 5).
        comment (str): The comment or review text.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        """
        Returns the string representation of the review.
        """
        return f"{self.user.username} - {self.track.title}"
