from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return self.name


class Projection(models.Model):
    movie = models.ForeignKey(Movie)
    _2D = 1
    _3D = 2
    _4D = 3
    _4DX = 4
    MOVIE_TYPES = (
        (_2D, '2D'),
        (_3D, '3D'),
        (_4D, '4D'),
        (_4DX, '4DX'),
    )
    type = models.SmallIntegerField(choices=MOVIE_TYPES, default=_2D, validators=[MinValueValidator(0)])
    date = models.DateTimeField()

    def __str__(self):
        return '{} | {} | {}'\
            .format(self.movie.name, self.get_type_display(), self.date)


class Reservation(models.Model):
    username = models.CharField(validators=[MinLengthValidator(3), ], max_length=25)
    projection = models.ForeignKey(Projection)
    row = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    col = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return 'User: {} | Projection: [{}] | Place:(row:{} col: {})'\
            .format(self.username, self.projection, self.row, self.col)
