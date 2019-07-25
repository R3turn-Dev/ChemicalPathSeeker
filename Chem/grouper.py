from typing import List, Union
from .prototype import Equation, ThermochemicalEquation
from .parser import Parser


class Grouper:
    def __init__(self, equations: List[Equation] = None):
        self.equations = [*equations] if equations else []

    def add_equation(self, equation: Union[str, Equation]):
        """
        Add an equation to class

        Parameters
        ----------
        equation: Union[str, Equation]
            An equation to add
        """
        # If string passed, parse it
        if isinstance(equation, str):
            parser = Parser()
            equation = parser.run(equation)

        # If parse fail thus not Equation
        if not isinstance(equation, Equation):
            print(f"{equation} is not an Equation.")

        # Else, append it to self.equations
        else:
            self.equations.append(equation)

    def estimate(self) -> List[Equation, ThermochemicalEquation]:
        """
        Estimate all the possible child occurrences of equations.

        Returns
        -------
        List[Equation, ThermochemicalEquation]
            Estimated equations
        """
        equations = self.equations
        if not equations:
            return []

        return []
