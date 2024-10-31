#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
General stats class.
"""
from core.dinosaur.Dinosaur import Dinosaur
from core.game.Reference import Reference


class Stats:
    dinosaur: Dinosaur
    attribute: str = Reference.health

    def __init__(self, dinosaur: Dinosaur):
        self.dinosaur = dinosaur

    def get_wild_stat(self) -> float:
        # wild_stat = base * (1 + (gain_per_level * points))
        # wild_stat: stat for specific attribute regarding the number of points assigned in the wild dinosaur.
        # base: each dinosaur has a base stat for each attribute.
        # gain_per_level: every dinosaur increase its stat based on this percentage.
        # points: number of points assigned to this stat.
        base: float = self.dinosaur.dinosaur.base_value.get_attribute_by(self.attribute)
        gain_per_level: float = self.dinosaur.dinosaurs.base_stat.get_attribute_by(self.attribute)
        points: float = self.dinosaur.dinosaur.wild_point.get_attribute_by(self.attribute)
        wild_stat: float = base * (1 + gain_per_level * points)
        wild_stat = round(wild_stat, 1)
        # print(f'### Wild value for {self.attribute} ###')
        # print(f'base: ------------ {base}')
        # print(f'gain_per_level: -  {gain_per_level}')
        # print(f'points: ---------- {points}')
        # print('wild_stat = base * (1 + (gain_per_level * points))')
        # print(f'{wild_stat} = {base} * (1 + ({gain_per_level} * {points}))')

        return wild_stat

    def get_tamed_leveled_stat(self, wild_stat: float) -> float:
        # tamed_stat = wild_stat * (1 + (gain_per_level * points))
        # wild_stat: stat for specific attribute regarding the number of points assigned in the wild dinosaur.
        # gain_per_level: every dinosaur increase its stat based on this percentage.
        # points: number of points assigned to this stat.
        gain_per_level: float = self.dinosaur.dinosaurs.tamed_stat.get_attribute_by(self.attribute)
        points: float = self.dinosaur.dinosaur.tamed_point.get_attribute_by(self.attribute)
        tamed_stat: float = wild_stat * (1 + gain_per_level * points)
        tamed_stat = round(tamed_stat, 1)
        # print(f'### Tamed leveled value for {self.attribute} ###')
        # print(f'wild_stat: ------- {wild_stat}')
        # print(f'gain_per_level: -  {gain_per_level}')
        # print(f'points: ---------- {points}')
        # print('tamed_stat = wild_stat * (1 + (gain_per_level * points))')
        # print(f'{tamed_stat} = {wild_stat} * (1 + ({gain_per_level} * {points}))')

        return tamed_stat

    def display_values(self, attribute: str):
        self.attribute: str = attribute
        wild_stat: float = self.get_wild_stat()
        tamed_leveled_stat: float = self.get_tamed_leveled_stat(wild_stat)
        print(f'Attribute: {self.attribute}')
        print(f'Wild attribute: {self.dinosaur.dinosaur.wild_point.get_attribute_by(attribute)}')
        print(f'Tamed attribute: {self.dinosaur.dinosaur.tamed_point.get_attribute_by(attribute)}')
        print(f'wild_stat: {wild_stat}')
        print(f'tamed_leveled_stat: {tamed_leveled_stat}')
        print()
