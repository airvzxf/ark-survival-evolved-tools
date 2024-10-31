#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
General server class.
"""
from core.dinosaur.Utility import Utility
from core.game.AttributeStats import AttributeStats


class Server:
    def __init__(self):
        class PerLevelStatsMultiplier(Utility, AttributeStats):
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

                class Player(Utility, AttributeStats):
                    def __init__(self):
                        self.health: float = 1.0
                        self.stamina: float = 1.0
                        self.torpidity: float = 1.0
                        self.oxygen: float = 1.0
                        self.food: float = 1.0
                        self.water: float = 1.0
                        self.temperature: float = 1.0
                        self.weight: float = 1.0
                        self.melee_damage_multiplier: float = 1.0
                        self.speed_multiplier: float = 1.0
                        self.temperature_fortitude: float = 1.0
                        self.crafting_speed_multiplier: float = 1.0
                        super().__init__(self)

                        self.player = Player()

                class DinoWild(Utility, AttributeStats):
                    def __init__(self):
                        self.health: float = 1.0
                        self.stamina: float = 1.0
                        self.torpidity: float = 1.0
                        self.oxygen: float = 1.0
                        self.food: float = 1.0
                        self.water: float = 1.0
                        self.temperature: float = 1.0
                        self.weight: float = 1.0
                        self.melee_damage_multiplier: float = 1.0
                        self.speed_multiplier: float = 1.0
                        self.temperature_fortitude: float = 1.0
                        self.crafting_speed_multiplier: float = 1.0
                        super().__init__(self)

                        self.dino_wild = DinoWild()

                class DinoTamed(Utility, AttributeStats):
                    def __init__(self):
                        self.health: float = 0.2
                        self.stamina: float = 1.0
                        self.torpidity: float = 1.0
                        self.oxygen: float = 1.0
                        self.food: float = 1.0
                        self.water: float = 1.0
                        self.temperature: float = 1.0
                        self.weight: float = 1.0
                        self.melee_damage_multiplier: float = 0.17
                        self.speed_multiplier: float = 1.0
                        self.temperature_fortitude: float = 1.0
                        self.crafting_speed_multiplier: float = 1.0
                        super().__init__(self)

                        self.dino_tamed = DinoTamed()

                class DinoTamedAdd(Utility, AttributeStats):
                    def __init__(self):
                        self.health: float = 0.14
                        self.stamina: float = 1.0
                        self.torpidity: float = 1.0
                        self.oxygen: float = 1.0
                        self.food: float = 1.0
                        self.water: float = 1.0
                        self.temperature: float = 1.0
                        self.weight: float = 1.0
                        self.melee_damage_multiplier: float = 0.14
                        self.speed_multiplier: float = 1.0
                        self.temperature_fortitude: float = 1.0
                        self.crafting_speed_multiplier: float = 1.0
                        super().__init__(self)

                        self.dino_tamed_add = DinoTamedAdd()

                class DinoTamedAffinity(Utility, AttributeStats):
                    def __init__(self):
                        self.health: float = 0.44
                        self.stamina: float = 1.0
                        self.torpidity: float = 1.0
                        self.oxygen: float = 1.0
                        self.food: float = 1.0
                        self.water: float = 1.0
                        self.temperature: float = 1.0
                        self.weight: float = 1.0
                        self.melee_damage_multiplier: float = 0.44
                        self.speed_multiplier: float = 1.0
                        self.temperature_fortitude: float = 1.0
                        self.crafting_speed_multiplier: float = 1.0
                        super().__init__(self)

                        self.dino_tamed_affinity = DinoTamedAffinity()

        self.per_level_stats_multiplier = PerLevelStatsMultiplier()
