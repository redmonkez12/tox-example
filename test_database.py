# from conftest import fake_user_db # neni potreba
# import conftest

from collections import namedtuple

Person = namedtuple("Person", "id name")

# person = Person(1, "Tomas")
# person.name
# person.id


# class Person:
#     def __init__(self, id: int, name: str) -> None:
#         self.id = id
#         self.name = name

# class - muzeme testy psat jako funkce nebo tridu a potom pro celou tridy jeden setup, teardown a sdilim data
# module - pro jeden soubor
# package - pro celou test slozku
# session - mam jedny data pro vsechny testy, vola se setup and teardown jednou

# bash

# vychozi nastaveni pro fixture je, ze se vola pro kazdy test zvlast
# a dostavame pokazde nova data


def test_add_person(fake_user_db: list[Person]):
    fake_user_db.append(Person(1, "Tomas"))

    assert len(fake_user_db) == 1


def test_add_another_person(fake_user_db: list[Person]):
    fake_user_db.append(Person(2, "Alfons"))

    assert len(fake_user_db) == 1
