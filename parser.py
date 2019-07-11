#
# Parser
# Author: Eunhak Lee(@return0927)
#
from Chem.status import *
from Chem.prototype import Atom, Compound, Equation
from traceback import format_exc


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

        # If indicating status or sth else
        if ("(" in data and ")" in data) and \
                0 <= data.index("(") < data.index(")") < len(data):
            compound, status = data[:data.index("(")], data[data.index("("):]

