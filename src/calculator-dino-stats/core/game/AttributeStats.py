#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Attribute class.
"""


class AttributeStats:
    def __init__(self):
        self.health: float = 375
        self.stamina: float = 150
        self.torpidity: float = 250
        self.oxygen: float = 150
        self.food: float = 3000
        self.water: float = 100
        self.temperature: float = 0
        self.weight: float = 365
        self.melee_damage_multiplier: float = 100
        self.speed_multiplier: float = 100
        self.temperature_fortitude: float = 0
        self.crafting_speed_multiplier: float = 100
