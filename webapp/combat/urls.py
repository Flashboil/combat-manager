from django.urls import path
from . import views

urlpatterns = [
    path('', views.characters_view, name='characters'),
    path('combat/<int:encounter_id>/', views.combat_view, name='combat'),
    path('combat/<int:encounter_id>/next_turn/', views.next_turn_view, name='next_turn'),
    path('combat/update_health/<int:combatant_id>/', views.update_health_view, name='update_health'),
]