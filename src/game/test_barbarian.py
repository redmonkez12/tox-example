from unittest.mock import Mock, patch

from weapon import Weapon
from barbarian import Barbarian
import pytest

# alt + enter
# option + enter


def test_attack_with_high_damage():
    weapon_damage = 25
    barbarian_damage = 60

    mock_weapon = Mock(spec=Weapon)
    mock_weapon.attack.return_value = weapon_damage

    barbarian = Barbarian(barbarian_damage, 60, mock_weapon)

    assert barbarian.attack() == weapon_damage + barbarian_damage + 15


# def test_attack_with_high_damage():

# with patch.object(Weapon, "attack") as mock_weapon:
#     mock_weapon.return_value = 25
#     weapon_damage = 25
#     barbarian_damage = 60

# mock_weapon = Mock(spec=Weapon)
# mock_weapon.attack.return_value = weapon_damage

# barbarian = Barbarian(barbarian_damage, 60, mock_weapon)

# assert barbarian.attack() == weapon_damage + barbarian_damage + 15


def test_attack_with_broken_weapon():
    mock_weapon = Mock(spec=Weapon)
    mock_weapon.attack.side_effect = Exception("Cannot attack")

    barbarian = Barbarian(60, 60, mock_weapon)

    # with pytest.raises(Exception, match="Cannot attack"):
    #     barbarian.attack()

    # with pytest.raises(Exception):
    result = barbarian.attack()
    assert result == 0

    # assert str(e.value) == "Cannot attack 1"
