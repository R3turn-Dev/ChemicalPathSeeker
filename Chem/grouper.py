from typing import List
from .prototype import Equation
from .parser import Parser


class Grouper:
    def __init__(self, equations: List[Equation] = None):
        self.equations = [*equations] if equations else []

    def add_equation(self, equation):
        if isinstance(equation, str):
            parser = Parser()
            equation = parser.run(equation)

        if not isinstance(equation, Equation):
            print(f"{equation} is not an Equation.")
        else:
            self.equations.append(equation)
