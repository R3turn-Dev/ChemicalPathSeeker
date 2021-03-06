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

    def estimate(self) -> List[Union[Equation, ThermochemicalEquation]]:
        """
        Estimate all the possible child occurrences of equations.

        Returns
        -------
        List[Union[Equation, ThermochemicalEquation]]
            Estimated equations
        """
        equations = [x for x in self.equations if isinstance(x, Equation)]
        equations = [ThermochemicalEquation.from_equation(x) if not hasattr(x, "enthalpy") else x for x in equations]
        if not equations:
            return []

        out = []
        for i in range(len(equations)):
            for j in range(i + 1, len(equations)):
                org = len(equations[i].reactants)
                org += len(equations[i].products)
                org += len(equations[j].reactants)
                org += len(equations[j].products)

                for eq in [equations[i] + equations[j], equations[i] - equations[j]]:
                    l = len(eq.reactants) + len(eq.products)
                    if l < org:
                        out.append(eq)

        return out
