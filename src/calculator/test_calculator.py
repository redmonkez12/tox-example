from _pytest.fixtures import SubRequest

from calculator import Calculator
import pytest


def format_output(data: tuple[float, float]) -> str:
    return f"Prvni cislo: {data[0]}, Druhe cislo {data[1]}"


# 1. Pristup je pomoci lambdy nebo funkce
# 2. Pristup je hardcoded values
# 3. str


@pytest.fixture(
    params=[(2, 5), (-3, -5), (4, 6)],
    # ids=lambda data: f"Prvni cislo: {data[0]}, Druhe cislo {data[1]}",
    # ids=format_output,
    ids=str,
)
def calculator(request: SubRequest):
    a, b = request.param
    calculator = Calculator(a, b)

    return calculator


def test_multiplication(calculator: Calculator):
    output = calculator.multiply()

    assert output == calculator.a * calculator.b


def test_addition(calculator: Calculator):
    output = calculator.add()

    assert output == calculator.a + calculator.b


def test_division(calculator: Calculator):
    output = calculator.divide()

    assert output == calculator.a / calculator.b


# Pro nejake edge case - kdyz potrebujete kontrolu nad parametry

# def pytest_generate_tests(metafunc):
#     if "calculator" in metafunc.fixturenames:
#         metafunc.parametrize("calculator, franta",
#                              [Calculator(2, 5), Calculator(-3, -5), Calculator(4, -6)],
#                              ids=["2, 5", "-3, -5", "4, -6"]
#                              )

# @pytest.mark.parametrize(
#     ["a", "b"],
#     [(2, 5), (-3, -5), (4, 6)],
#     ids=["2 * 5 = 10", "-3 * -5 - 15", "4 * 6 = 24"],
# )
# # @pytest.mark.parametrize("a, b")
# def test_multiplication(a: float, b: float):
#     calculator = Calculator(a, b)
#     output = calculator.multiply()
#
#     assert output == a * b


def test_multiplication_with_positive_numbers():
    calculator = Calculator(2, 5)
    output = calculator.multiply()
    assert output == 10

    # data = [(2, 5), (-3, -5), (4, 6)]
    #
    # for numbers in data:
    #     calculator = Calculator(numbers[0], numbers[1])
    #     output = calculator.multiply()
    #     assert output == 10


def test_multiplication_with_negative_numbers():
    calculator = Calculator(-3, -5)
    output = calculator.multiply()
    assert output == 15


def test_multiplication_with_negative_and_positive_number():
    calculator = Calculator(4, -6)
    output = calculator.multiply()
    assert output == -24
