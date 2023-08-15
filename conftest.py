import pytest
import time


@pytest.fixture()  # decorator
def fake_user_db():
    """Poskytuje uzivatelske data z docasne databaze"""
    people = []

    # print("Connecting to database")
    time.sleep(1)

    yield people  # generator

    # print("Closing database...")
    time.sleep(1)

    # return people


@pytest.fixture(autouse=True)
def measure_time():
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print(delta)
