#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main module
"""
import numpy as np
from matplotlib import pyplot as plt

from core.dinosaur.Dinosaur import Dinosaur
from core.game.Reference import Reference
from core.stats.Stats import Stats


def main(name):
    print(f'Hi, {name}')
    print()
    dinosaur = Dinosaur('Triceratops')

    dinosaur.dinosaur.wild_point.melee_damage_multiplier = 0
    dinosaur.dinosaur.tamed_point.melee_damage_multiplier = 5
    stats = Stats(dinosaur)
    stats.display_values(Reference.melee_damage_multiplier)

    wild_level = 24 + 1
    tamed_level = 150 + 1
    data = np.zeros((tamed_level, wild_level), dtype=float)
    print(f'data: {data.shape}')

    for wild_point in range(0, wild_level):
        for tamed_point in range(0, tamed_level):
            total_points = wild_point + tamed_point + 1
            if total_points > tamed_level:
                continue
            # dinosaur.dinosaur.wild_point.melee_damage_multiplier = wild_point
            # dinosaur.dinosaur.tamed_point.melee_damage_multiplier = tamed_point
            # wild_stat: float = stats.get_wild_stat()
            # tamed_leveled_stat: float = stats.get_tamed_leveled_stat(wild_stat)
            attribute = dinosaur.dinosaur.base_value.stamina
            wild_stat = attribute * (1 + (0.1 * wild_point))
            wild_stat = round(wild_stat, 1)
            tamed_leveled_stat = wild_stat * (1 + (0.1 * tamed_point))
            tamed_leveled_stat = round(tamed_leveled_stat, 1)
            # print(f'Wild pts: {wild_point}'
            #       f' | Tamed pts: {tamed_point}'
            #       f' | Tamed stat: {tamed_leveled_stat}'
            #       f' | Points: {wild_point + tamed_point}')
            data[tamed_point, wild_point] = tamed_leveled_stat

    # exit()
    max_value = data.max()
    mean_value = data.mean()
    min_value = np.min(data[np.nonzero(data)])
    print(f'Min value: {min_value}')
    print(f'Mean value: {mean_value}')
    print(f'Max value: {max_value}')
    # min_value = max_value * 0.95
    # print(f'Min value: {min_value}')

    # data = data[(data > min_value).any(axis=1), :]
    # print(f'Final stats: {data.shape}')
    # data = data[:, (data > min_value).any(axis=0)]
    # print(f'Final stats: {data.shape}')

    title = f'Triceratops: stat {Reference.stamina.title()} (min: {min_value} | max: {max_value})'
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel('Wild points')
    ax.set_ylabel('Tamed points')

    # plt.imshow(data, cmap='viridis')
    # plt.imshow(data, cmap='hot', interpolation='nearest')
    # plt.imshow(data, cmap='rainbow', interpolation='nearest')
    plt.pcolormesh(data, cmap='RdBu')
    plt.colorbar()

    # ax.matshow(data)
    # ax.plot(data)
    plt.show()


if __name__ == '__main__':
    main('Triceratops')
