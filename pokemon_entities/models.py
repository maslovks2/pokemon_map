from django.db import models


class Pokemon(models.Model):

    title_ru = models.CharField(max_length=200, verbose_name="Имя (рус.)")
    title_en = models.CharField(max_length=200, blank=True, verbose_name="Имя (англ.)")
    title_jp = models.CharField(max_length=200, blank=True, verbose_name="Имя (яп.)")
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение")
    description = models.TextField(blank=True, verbose_name="Описание")

    previous_evolution = models.OneToOneField(
        "self", 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name="next_evolution",
        verbose_name="Из кого эволюционировал"
    )

    def __str__(self):
        return self.title_ru

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

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name="Покемон")
    
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")

    appeared_at = models.DateTimeField(verbose_name="Появляется с", null=True, blank=True)
    dissappeared_ad = models.DateTimeField(verbose_name="Исчезает после", null=True, blank=True)

    level = models.IntegerField(verbose_name="Уровень", null=True, blank=True)
    health = models.IntegerField(verbose_name="Здоровье", null=True, blank=True)
    strength = models.IntegerField(verbose_name="Сила", null=True, blank=True)
    defence = models.IntegerField(verbose_name="Защита", null=True, blank=True)
    stamina = models.IntegerField(verbose_name="Выносливость", null=True, blank=True)
