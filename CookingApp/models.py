from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    recipeTitle = models.CharField(max_length = 100)
    shortDescription = models.CharField(max_length = 255, default='SOME STRING')
    ingredients = models.TextField()
    description = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)

    def __str__ (self):
        return self.recipeTitle

    class Meta:
        db_table='Recipe'
        verbose_name_plural = 'Recipes'

class Review(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='reviews', on_delete = models.DO_NOTHING)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 255)
    rating = models.SmallIntegerField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)

    def __str__ (self):
        return self.title

    class Meta:
        db_table='Review'
        verbose_name_plural = 'Reviews'



