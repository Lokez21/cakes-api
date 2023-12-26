from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Cake(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    comment = models.CharField(max_length=200, blank=False, null=False)
    image_url = models.CharField(max_length=500, blank=False, null=False)
    yum_factor = models.IntegerField(
        validators=[
            MinValueValidator(1, message='Value must be greater than or equal to 1.'),
            MaxValueValidator(5, message='Value must be less than or equal to 5.'),
        ],
        help_text='Enter an integer between 1 and 5 (inclusive).',
        blank=False,
        null=False,
    )

    def __str__(self):
        return f'[{self.pk}] {self.name}'
