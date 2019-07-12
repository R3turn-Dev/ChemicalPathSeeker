#
# Parser
# Author: Eunhak Lee(@return0927)
#
from .status import *
from .prototype import Atom, Compound, Equation
from traceback import format_exc
from .exception import ParseError


class Parser:
    def __init__(self):
        self.algorithm = []
        self.status = 0

    def run(self, data):
        self.status = 1

        try:
            for func in self.algorithm:
                data = func(data)

            self.status = 0
        except:
            self.status = -1

            data = format_exc()

        finally:
            return data

    @staticmethod
    def separate_compounds(data):
        """

        :param data: string of compounds or an equation
        :return: Compound or Equation
        """
        # Equation mode
        if "->" in data:
            before, after = data.split("->")
            before = [x.strip() for x in before.split("+")]
            after = [x.strip() for x in after.split("+")]

        # Compounds mode
        else:
            compounds = [x.split() for x in data.split("+")]

    @staticmethod
    def parse_compound(data):
        """Convert compound string into compound class

        :param data: string of a compound
        :return: class Chem.prototype.Compound
        """
        count = 1

        # Starting with count of compound
        if data[0].isnumeric():
            count = int(data[0])
            data = data[1:]

        compound = data
        status = "(g)"
        # If indicating status or sth else
        if ("(" in compound and ")" in compound) and \
                0 <= compound.index("(") < compound.index(")") < len(compound):
            compound, status = compound[:compound.index("(")], compound[compound.index("("):]

    @staticmethod
    def parse_status(data):
        """Convert () stripped string into status and meta information

        :param data: () stripped string
        :return: parsed data as [Chem.status.Status, str]
        """
        if not (data[0] == "(" and data[-1] == ")"):
            raise ParseError("Unexpected status string passed", data=data)


