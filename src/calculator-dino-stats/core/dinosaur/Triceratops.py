#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Triceratops class.
"""
from core.dinosaur.Utility import Utility
from core.game.AttributeStats import AttributeStats


class Triceratops:
    def __init__(self):
        self.level: int = 1

        class BaseValue(Utility, AttributeStats):
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
                super().__init__(self)

        class WildPoint(Utility, AttributeStats):
            def __init__(self):
                self.health: float = 0
                self.stamina: float = 0
                self.torpidity: float = 0
                self.oxygen: float = 0
                self.food: float = 0
                self.water: float = 0
                self.temperature: float = 0
                self.weight: float = 0
                self.melee_damage_multiplier: float = 0
                self.speed_multiplier: float = 0
                self.temperature_fortitude: float = 0
                self.crafting_speed_multiplier: float = 0
                super().__init__(self)

        class TamedPoint(Utility, AttributeStats):
            def __init__(self):
                self.health: float = 0
                self.stamina: float = 0
                self.torpidity: float = 0
                self.oxygen: float = 0
                self.food: float = 0
                self.water: float = 0
                self.temperature: float = 0
                self.weight: float = 0
                self.melee_damage_multiplier: float = 0
                self.speed_multiplier: float = 0
                self.temperature_fortitude: float = 0
                self.crafting_speed_multiplier: float = 0
                super().__init__(self)

        self.base_value = BaseValue()
        self.wild_point = WildPoint()
        self.tamed_point = TamedPoint()
