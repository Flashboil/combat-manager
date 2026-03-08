from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=50)
    max_hp = models.IntegerField()
    current_hp = models.IntegerField()
    armor = models.IntegerField()
    level = models.IntegerField()

    def __str__(self):
        return f"{self.name} - lvl {self.level} AC: {self.armor} HP: {self.current_hp} / {self.max_hp}"
    
class Encounter(models.Model):
    name = models.CharField(max_length=200)
    current_turn = models.IntegerField(default=0)
    round_number = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Combatant(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    encounter = models.ForeignKey(Encounter, on_delete=models.CASCADE)
    initiative = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.character.name} in {self.encounter.name}"
