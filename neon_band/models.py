
from django.db import models
from django.contrib.auth.models import User

class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    origin = models.CharField(max_length=100)
    formation_date = models.DateField()
    biography = models.TextField()
    social_media_links = models.URLField()

    def __str__(self):
        return self.name

class Track(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    release_date = models.DateField()
    audio_file = models.FileField(upload_to='music/')

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_tracks = models.ManyToManyField(Track)

    def __str__(self):
        return self.user.username

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.track.title}"
