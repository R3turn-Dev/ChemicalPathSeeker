#
# Chem.prototype
# Author: Eunhak Lee(@return0927)
#
from .status import Status
from .atoms import Element
from .periodictable import TABLE, NAME2NUM
from typing import List
from collections import OrderedDict


class CountedDict(OrderedDict):
    def __add__(self, other):
        out = self.copy()

        for k, v in other.items():
            if k in out:
                out[k].count += v.count
            else:
                out[k] = v

        return out


class Atom(Element):
    def __repr__(self):
        return f"""class <Atom({self.atomic_repr}, {self.atomic_number})>"""

    def __str__(self):
        return self.atomic_repr

    def __init__(self, no):
        super().__init__(no)

        self.electrons = self.atomic_number

    @property
    def atomic_repr(self):
        return repr(TABLE[self.atomic_number]())

    @property
    def atomic_name(self):
        return TABLE[self.atomic_number].atomic_name

    @property
    def proton(self):
        return self.atomic_number

    @staticmethod
    def derive_from_atomic_number(num):
        return Atom(num)

    @staticmethod
    def derive_from_atomic_repr(string):
        return Atom(NAME2NUM[string])


class Compound:
    def __repr__(self):
        return f"class <Compound({self.chemical_formula}))>"

    def __str__(self):
        return repr(self)

    def __add__(self, other):
        atoms = self.atoms.copy()

        for atom in other.atoms:
            if atom.atomic_number not in atoms:
                atoms[atom.atomic_number] = 0

            atoms[atom.atom.atomic_number] += 1

        return Compound.from_ordered_dict(atoms)

    @property
    def chemical_formula(self):
        out = str(self.count) if self.count > 1 else ""

        for k, v in self.atoms.items():
            if not v:
                continue

            out += "{}{}".format(Atom.derive_from_atomic_number(k).atomic_repr, v if v > 1 else "")

        return out + str(self.status)

    @staticmethod
    def from_ordered_dict(atoms: OrderedDict, count: int = 1, status: Status = Status()):
        _atoms = []

        for k, v in atoms:
            for n in range(v):
                _atoms.append(Atom.derive_from_atomic_number(k))

        return Compound(_atoms, count, status)

    @staticmethod
    def from_chemical_formula(formula: str, count: int = 1, status: Status = Status()):
        pass

    def __init__(self, atoms: List[Atom], count: int = 1, status: Status = Status()):
        self.count = count
        self.status = status
        self.atoms = OrderedDict()

        for atom in atoms:
            if atom.atomic_number not in self.atoms:
                self.atoms[atom.atomic_number] = 0

            self.atoms[atom.atomic_number] += 1


class Equation:
    reactants: List[Compound]
    products: List[Compound]

    def __repr__(self):
        return f"""class {self.__class__.__name__}<{str(self)}>"""

    def __str__(self):
        return "{} -> {}".format(
            " + ".join([x.chemical_formula for x in self.reactants]),
            " + ".join([x.chemical_formula for x in self.products])
            )

    def __add__(self, other):
        reactants = CountedDict(
            (x.chemical_formula[1:] if x.count > 1 else x.chemical_formula, x) for x in self.reactants
            ) + CountedDict(
            (x.chemical_formula[1:] if x.count > 1 else x.chemical_formula, x) for x in other.reactants
            )

        products = CountedDict(
            (x.chemical_formula[1:] if x.count > 1 else x.chemical_formula, x) for x in self.products
            ) + CountedDict(
            (x.chemical_formula[1:] if x.count > 1 else x.chemical_formula, x) for x in other.products
            )

        for elem in {*reactants} & {*products}:
            if reactants[elem].count > products[elem].count:
                reactants[elem].count -= products[elem].count
                del products[elem]
            else:
                products[elem].count -= reactants[elem].count
                del reactants[elem]

        return Equation([*reactants.values()], [*products.values()])

    def __sub__(self, other):
        return self + other.reverse()

    def __init__(self, reactants: List[Compound], products: List[Compound]):
        self.reactants = [*reactants]
        self.products = [*products]

    def reverse(self):
        return Equation(self.products, self.reactants)


class ThermochemicalEquation(Equation):
    def __str__(self):
        return "{} -> {}, ΔH = {}".format(
            " + ".join([x.chemical_formula for x in self.reactants]),
            " + ".join([x.chemical_formula for x in self.products]),
            "{:,}kJ".format(self.enthalpy / 1e3) if abs(self.enthalpy) > 1e3 else
            "{:,}J".format(self.enthalpy)
            )

    def __add__(self, other):
        return ThermochemicalEquation.from_equation(
            Equation.__add__(self, other),
            enthalpy=self.enthalpy + other.enthalpy,
            )

    def __init__(self, reactants: List[Compound], products: List[Compound], enthalpy: int = 0):
        super().__init__(reactants, products)
        self.enthalpy = enthalpy

    @staticmethod
    def from_equation(equation: Equation, enthalpy: int = 0):
        return ThermochemicalEquation(equation.reactants, equation.products, enthalpy)

    def reverse(self):
        return ThermochemicalEquation(self.products, self.reactants, -self.enthalpy)
