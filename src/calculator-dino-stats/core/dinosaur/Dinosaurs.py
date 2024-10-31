#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
General dinosaur class.
"""
from core.dinosaur.Utility import Utility
from core.game.AttributeStats import AttributeStats


class Dinosaurs:
    def __init__(self):
        super().__init__()

        class BaseStat(Utility, AttributeStats):
            def __init__(self):
                self.health: float = 0.2
                self.stamina: float = 0.1
                self.torpidity: float = 0.0
                self.oxygen: float = 0.1
                self.food: float = 0.1
                self.water: float = 0.0
                self.temperature: float = 0.0
                self.weight: float = 0.02
                self.melee_damage_multiplier: float = 0.05
                self.speed_multiplier: float = 0.0
                self.temperature_fortitude: float = 0.0
                self.crafting_speed_multiplier: float = 0.0
                super().__init__(self)

        class TamedStat(Utility, AttributeStats):
            def __init__(self):
                self.health: float = 0.0621
                self.stamina: float = 0.1
                self.torpidity: float = 0.0
                self.oxygen: float = 0.1
                self.food: float = 0.1
                self.water: float = 0.0
                self.temperature: float = 0.0
                self.weight: float = 0.04
                self.melee_damage_multiplier: float = 0.02
                self.speed_multiplier: float = 0.025
                self.temperature_fortitude: float = 0.0
                self.crafting_speed_multiplier: float = 0.0
                super().__init__(self)

        self.base_stat = BaseStat()
        self.tamed_stat = TamedStat()
