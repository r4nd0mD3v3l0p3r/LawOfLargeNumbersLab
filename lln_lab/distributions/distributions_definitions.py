from enum import Enum


class Distribution(Enum):
    UNIFORM = ("uniform", "U(0,1)")
    Z = ("z", "Z")
    EXPONENTIAL = ("exponential", "Exp(1)")
    GAMMA = ("gamma", "Gamma(2, 2)")

    def __init__(self, key, label):
        self.key = key
        self.label = label

    def __str__(self):
        return self.label
