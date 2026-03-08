from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404

from .forms import CharacterForm, CombatantForm, EncounterForm
from .models import Character, Combatant, Encounter

def characters_view(request):

    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()

    form = CharacterForm()
    characters = Character.objects.all()

    return render(request, 'combat/characters.html', {
        'form': form,
        'characters': characters
    })

def combat_view(request, encounter_id):

    encounter = Encounter.objects.get(id=encounter_id)

    combatants = Combatant.objects.filter(encounter=encounter).order_by('-initiative')

    return render(request, 'combat/combat.html', {
        'encounter': encounter,
        'combatants': combatants
    })

def next_turn_view(request, encounter_id):

    encounter = Encounter.objects.get(id=encounter_id)

    combatants = Combatant.objects.filter(encounter=encounter)

    encounter.current_turn += 1

    if encounter.current_turn >= combatants.count():
        encounter.current_turn = 0
        encounter.round_number += 1

    encounter.save()

    return redirect('combat', encounter_id=encounter.id)

def update_health_view(request, combatant_id):
    if request.method == 'POST':
        combatant = get_object_or_404(Combatant, id=combatant_id)
        
        try:
            change = int(request.POST.get('change', 0))
        except ValueError:
            change = 0
        
        combatant.character.current_hp += change
        
        if combatant.character.current_hp < 0:
            combatant.character.current_hp = 0
        elif combatant.character.current_hp > combatant.character.max_hp:
            combatant.character.current_hp = combatant.character.max_hp
        
        combatant.character.save()
        
        return redirect('combat', encounter_id=combatant.encounter.id)
    
    return redirect('combat', encounter_id=combatant.encounter.id)