import random


class Weapon:
    def __init__(
        self, strength: int, endurance: int, width: float = 0, height: float = 0
    ) -> None:
        self._health = 100
        self._strength = strength
        self._endurance = endurance
        self._width = width
        self._height = height

    def attack(self) -> float:
        print(self._health, "tady bych to mel videt")
        print(self._strength, "toto bych tady taky mel videt")

        # if self._health < 10:
        #     return 0

        if self._health < 10:
            raise Exception("Cannot attack")

        value = random.randint(0, self._endurance)

        if value < (self._endurance // 2):
            self._health -= 1

        bonus_damage = random.randint(0, 20)

        return self._strength + bonus_damage
