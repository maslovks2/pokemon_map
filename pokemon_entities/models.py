from django.db import models


class Pokemon(models.Model):

    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    
    lat = models.FloatField()
    lon = models.FloatField()

    appeared_at = models.DateTimeField()
    dissappeared_ad = models.DateTimeField()

    level = models.IntegerField()
    health = models.IntegerField()
    strength = models.IntegerField()
    defence = models.IntegerField()
    stamina = models.IntegerField()

