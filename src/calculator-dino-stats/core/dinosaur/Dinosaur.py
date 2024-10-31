#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
General dinosaur class.
"""
from core.dinosaur.Dinosaurs import Dinosaurs
from core.dinosaur.Triceratops import Triceratops
from core.server.Server import Server


class Dinosaur:
    def __init__(self, dinosaur: str):
        self.dinosaurs = Dinosaurs()
        self.server = Server()

        if dinosaur.lower() == 'triceratops':
            self.dinosaur = Triceratops()
        else:
            raise Exception('Invalid dinosaur.')
