from django.db import models


class Pokemon(models.Model):

    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(blank=True)

    previous_evolution = models.OneToOneField(
        "self", 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        verbose_name="Из кого эволюционировал"
    )

    def __str__(self):
        return self.title_ru

    @property
    def next_evolution(self):
        try:
            return Pokemon.objects.get(previous_evolution=self)
        except Pokemon.DoesNotExist:
            return

    def to_dict(self, request=None):
        pokemon = {
            'pokemon_id': self.id,
            'image': self.image,
            'title_ru': self.title_ru,
            'title_en': self.title_en,
            'title_jp': self.title_jp,
            'description': self.description,
        }
        if request:
            pokemon['img_url'] = request.build_absolute_uri(self.image.url)
        return pokemon

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

