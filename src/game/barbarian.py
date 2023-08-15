from weapon import Weapon


class Barbarian:
    def __init__(self, strength: int, stamina: int, weapon: Weapon) -> None:
        self._health = 100
        self._strength = strength
        self._stamina = stamina
        self._weapon = weapon

    def attack(self) -> float:
        if not self._weapon:
            return 0

        try:
            damage = self._weapon.attack() + self._strength
        except Exception:
            return 0

        # damage = self._weapon.attack() + self._strength

        if damage > 15 and self._strength > 50 and self._stamina > 50:
            damage += 15
        elif self._stamina > 30:
            damage += 5

        return damage

        # if not self._weapon:
        #     raise Exception("Cannot attack")


# UML

# ctrl + b

# conan = Barbarian()
# value, error = conan.attack()

# if error != null:
#     # nejak zareagujete
#     # panic("gdfkgjfdglkdf")
#     if error != null:
#         if error != null:
#             if error != null:
#                 if error != null:
#
#                     if error != null:
#             if error != null:
#         if error != null:
#     if error != null:
