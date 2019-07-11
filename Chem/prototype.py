#
# Chem.prototype
# Author: Eunhak Lee(@return0927)
#
from .status import Status
from .atoms import Element
from .periodictable import TABLE
from typing import List


class Atom(Element):
    def __repr__(self):
        return f"""class <Atom({self.atomic_repr}{self.atomic_number})>"""

    def __str__(self):
        return repr(self)

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


class Compound:
    def __repr__(self):
        return f"""class <Compound({", ".join([repr(x) for x in self.atoms])})>"""

    def __str__(self):
        return repr(self)

    def __init__(self, atoms: List[Atom], status: Status = Status()):
        self.atoms = atoms
        self.status = status
