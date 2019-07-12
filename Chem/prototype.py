#
# Chem.prototype
# Author: Eunhak Lee(@return0927)
#
from .status import Status
from .atoms import Element
from .periodictable import TABLE, NAME2NUM
from typing import List


class Atom(Element):
    def __repr__(self):
        return f"""class <Atom({self.atomic_repr}{self.atomic_number})>"""

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
        return "class <Compound({}{}({}{}))>".format(
            self.count if self.count > 1 else "",
            "".join([str(x) for x in self.atoms]),
            self.status.status,
            ", " + self.status.meta if self.status.meta else ""
            )

    def __str__(self):
        return repr(self)

    def __init__(self, atoms: List[Atom], count: int = 1, status: Status = Status()):
        self.count = count
        self.atoms = [*atoms]
        self.status = status


class Equation:
    def __repr__(self):
        return f"""class <Equation({" + ".join(self.before)} -> {" + ".join(self.after)})>"""

    def __init__(self, before_compounds: List[Compound], after_compounds: List[Compound]):
        self.before = [*before_compounds]
        self.after = [*after_compounds]
