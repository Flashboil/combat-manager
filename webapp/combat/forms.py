from django import forms
from .models import Character, Encounter, Combatant


class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ['name', 'max_hp', 'current_hp', 'armor', 'level']

class EncounterForm(forms.ModelForm):
    class Meta:
        model = Encounter
        fields = ['name']

class CombatantForm(forms.ModelForm):
    class Meta:
        model = Combatant
        fields = ['character', 'initiative']

    def __init__(self, *args, **kwargs):
        encounter = kwargs.pop('encounter', None)
        super().__init__(*args, **kwargs)
        self.fields['character'].queryset = Character.objects.all()