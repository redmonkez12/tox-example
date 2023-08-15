class Calculator:
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def add(self) -> float:
        return self.a + self.b

    def multiply(self) -> float:
        return self.a * self.b

    def subtract(self) -> float:
        return self.a - self.b

    def divide(self) -> float:
        if self.b == 0:
            return 0

        return self.a / self.b


# line coverage - pocet otestovanych radku / pocet celkovych radku v kodu
# branch coverage - pocet projitych vetvi / pocet celkovych vetvi v kodu
