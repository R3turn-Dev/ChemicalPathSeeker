#
# Parser
# Author: Eunhak Lee(@return0927)
#
from Chem.status import *
from Chem.prototype import Atom, Compound
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


