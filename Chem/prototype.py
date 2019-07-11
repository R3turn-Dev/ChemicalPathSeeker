#
# Chem.prototype
# Author: Eunhak Lee(@return0927)
#
from .status import Status
from .periodictable import NUM2NAME, NUM2REPR
from typing import List


class Atom:
    def __repr__(self):
        return f"""class <Atom({self.atomic_repr}{self.atomic_number})>"""

    def __str__(self):
        return repr(self)

    def __init__(self, no):
        self.atomic_number = no

    @property
    def atomic_repr(self):
        return NUM2NAME[self.atomic_number]

    @property
    def atomic_name(self):
        return NUM2REPR[self.atomic_number]


class Compound:
    def __repr__(self):
        return f"""class <Compound({", ".join(self.atoms)})>"""

    def __str__(self):
        return repr(self)

    def __init__(self, atoms: List[Atom], status: Status = Status()):
        self.atoms = atoms
        self.status = status
