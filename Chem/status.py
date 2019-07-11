#
# Chem.status
# Author: Eunhak Lee(@return0927)
#


class Status:
    status = ""

    def __init__(self, temp=273):
        self.temperature = temp


class Gas(Status):
    status = "g"


class Liquid(Status):
    status = "l"


class Solid(Status):
    status = "s"


class Aqua(Status):
    status = "aq"
