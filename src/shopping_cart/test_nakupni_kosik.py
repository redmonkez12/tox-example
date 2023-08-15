import pytest
from nakupni_kosik import ShoppingCart, Product


def test_add_item():
    cart = ShoppingCart(10)
    rohlik = Product("rohlik normalni", 2.5)

    cart.add_item(rohlik, 9)

    assert len(cart.items) == 1


def test_add_two_same_items():
    cart = ShoppingCart(10)
    rohlik = Product("rohlik normalni", 2.5)

    cart.add_item(rohlik, 9)
    cart.add_item(rohlik, 1)

    assert cart.items[rohlik] == 10


def test_add_two_different_items():
    cart = ShoppingCart(20)
    rohlik = Product("rohlik normalni", 2.5)
    chleba = Product("chleba velky", 40)

    cart.add_item(rohlik, 9)
    cart.add_item(chleba, 2)

    assert cart.items[rohlik] + cart.items[chleba] == 11


def test_add_more_than_capacity():
    with pytest.raises(Exception) as ex:
        cart = ShoppingCart(10)
        rohlik = Product("rohlik normalni", 2.5)
        chleba = Product("chleba velky", 40)

        cart.add_item(rohlik, 9)
        cart.add_item(chleba, 2)

    assert str(ex.value) == "Toto se ti nevleze do kosiku"


def test_remove_item():
    cart = ShoppingCart(10)
    rohlik = Product("rohlik normalni", 2.5)

    cart.add_item(rohlik, 9)
    cart.remove_item(rohlik, 4)

    assert cart.items[rohlik] == 5


def test_get_total_count():
    rohlik = Product("rohlik normalni", 2.5)
    chleba = Product("chleba velky", 40)
    pepsi = Product("pepsi", 32)

    cart = ShoppingCart(30)

    cart.add_item(rohlik, 10)
    cart.add_item(chleba, 1)
    cart.add_item(pepsi, 2)

    assert cart.get_total_count() == 13


def test_get_total_price():
    rohlik = Product("rohlik normalni", 2.5)
    chleba = Product("chleba velky", 40)
    pepsi = Product("pepsi", 32)

    cart = ShoppingCart(30)

    cart.add_item(rohlik, 10)  # 25
    cart.add_item(chleba, 1)  # 40
    cart.add_item(pepsi, 2)  # 64

    assert cart.get_total_price() == 129


def test_remove_existing_item():
    cart = ShoppingCart(10)
    jablko = Product("jablko cervene", 12)

    cart.add_item(jablko, 10)
    cart.remove_item(jablko, 5)

    assert cart.items[jablko] == 5


def test_remove_nonexistent_item():
    with pytest.raises(Exception) as ex:
        cart = ShoppingCart(10)
        jablko = Product("jablko cervene", 12)
        hruska = Product("hruska recko", 8)

        cart.add_item(jablko, 5)
        cart.remove_item(hruska, 1)

    assert str(ex.value) == "Tato polozka neni v kosiku"
