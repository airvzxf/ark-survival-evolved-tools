#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Parasaur class.
"""
from core.game.Reference import Reference
from core.dinosaur.Dinosaurs import Dinosaurs


class Parasaur(Dinosaurs):
    attributes: dict = {
        Reference.base_value: {
            Reference.health: 200,
            Reference.stamina: 450,
            Reference.torpidity: 150,
            Reference.oxygen: 150,
            Reference.food: 1500,
            Reference.water: 100,
            Reference.temperature: 0,
            Reference.weight: 480,
            Reference.melee_damage_multiplier: 100,
            Reference.speed_multiplier: 100,
            Reference.temperature_fortitude: 0,
            Reference.crafting_speed_multiplier: 100,
        },
        Reference.wild_point: {
            Reference.health: 40,
            Reference.stamina: 45,
            Reference.torpidity: 9,
            Reference.oxygen: 15,
            Reference.food: 150,
            Reference.water: 0,
            Reference.temperature: 0,
            Reference.weight: 9.6,
            Reference.melee_damage_multiplier: 0.6,
            Reference.speed_multiplier: 0,
            Reference.temperature_fortitude: 0,
            Reference.crafting_speed_multiplier: 0,
        },
        Reference.tamed: {
            Reference.health: 5.4,
            Reference.stamina: 10,
            Reference.torpidity: 0,
            Reference.oxygen: 10,
            Reference.food: 10,
            Reference.water: 0,
            Reference.temperature: 0,
            Reference.weight: 4,
            Reference.melee_damage_multiplier: 1.7,
            Reference.speed_multiplier: 1,
            Reference.temperature_fortitude: 0,
            Reference.crafting_speed_multiplier: 0,
        },
        Reference.taming_bonus_additive: {
            Reference.health: 7,
            Reference.stamina: 0,
            Reference.torpidity: 50,
            Reference.oxygen: 0,
            Reference.food: 0,
            Reference.water: 0,
            Reference.temperature: 0,
            Reference.weight: 0,
            Reference.melee_damage_multiplier: 7,
            Reference.speed_multiplier: 67,
            Reference.temperature_fortitude: 0,
            Reference.crafting_speed_multiplier: 0,
        },
        Reference.taming_bonus_multiplicative: {
            Reference.health: 0,
            Reference.stamina: 0,
            Reference.torpidity: 0,
            Reference.oxygen: 0,
            Reference.food: 0,
            Reference.water: 0,
            Reference.temperature: 0,
            Reference.weight: 0,
            Reference.melee_damage_multiplier: 17.6,
            Reference.speed_multiplier: 0,
            Reference.temperature_fortitude: 0,
            Reference.crafting_speed_multiplier: 0,
        },
    }

    def __init__(self, attributes: dict = None):
        if attributes:
            self.attributes = attributes
