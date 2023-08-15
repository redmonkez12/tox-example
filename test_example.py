from test_database import Person


def test_user_data(fake_user_db):
    fake_user_db.append(Person(1, "Ferenc"))

    assert fake_user_db[0] == Person(1, "Ferenc")
