from weapon import Weapon
from unittest.mock import patch
import random


def test_attack_with_broken_weapon():
    weapon = Weapon(10, 20)
    # weapon._health = 5

    with patch.object(weapon, "_health", 5):  # context manager
        assert weapon.attack() == 0

    # prvni mockovani - mockovani property na objektu


# def test_weapon_weapon_damage():
#     weapon = Weapon(10, 20)
#
#     with patch.object(random, "randint", return_value=8):
#         damage = weapon.attack()
#
#         assert damage == 10
#         assert weapon._health == 99


def test_weapon_weapon_damage():
    weapon = Weapon(strength=10, endurance=20)

    with patch.object(random, "randint", side_effect=[8, 2]):
        damage = weapon.attack()

        assert damage == 12
        assert weapon._health == 99
