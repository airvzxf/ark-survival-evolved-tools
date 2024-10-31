#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
General utility class.
"""
from core.game.AttributeStats import AttributeStats
from core.game.Reference import Reference


class Utility:
    def __init__(self, child: AttributeStats):
        self.child = child

    def get_attribute_by(self, text: str) -> float:
        if text == Reference.health:
            return self.child.health
        elif text == Reference.stamina:
            return self.child.stamina
        elif text == Reference.torpidity:
            return self.child.torpidity
        elif text == Reference.oxygen:
            return self.child.oxygen
        elif text == Reference.food:
            return self.child.food
        elif text == Reference.water:
            return self.child.water
        elif text == Reference.temperature:
            return self.child.temperature
        elif text == Reference.weight:
            return self.child.weight
        elif text == Reference.melee_damage_multiplier:
            return self.child.melee_damage_multiplier
        elif text == Reference.speed_multiplier:
            return self.child.speed_multiplier
        elif text == Reference.temperature_fortitude:
            return self.child.temperature_fortitude
        elif text == Reference.crafting_speed_multiplier:
            return self.child.crafting_speed_multiplier
        else:
            raise ValueError(f'The attribute "{text}" is not in this class.')
