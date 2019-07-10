#
# Chem.prototype
# Author: Eunhak Lee(@return0927)
#
from .status import Status


class Atom:
    def __repr__(self):
        return f"""class <Atom({self.atomic_name}{self.atomic_number})>"""

    def __str__(self):
        return repr(self)

    def __init__(self, no):
        self.atomic_number = no
        self.atomic_name = ""


class Compound:
    def __repr__(self):
        return f"""class <Compound({", ".join(self.atoms)})>"""

    def __str__(self):
        return repr(self)

    def __init__(self, atoms, status: Status = Status()):
        self.atoms = atoms
        self.status = status
