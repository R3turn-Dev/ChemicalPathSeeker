#
# Chem.status
# Author: Eunhak Lee(@return0927)
#


class Status:
    status = ""
    temperature = 273


class Gas(Status):
    status = "g"

    def __init__(self, temperature=super().temperature):
        self.temperature = temperature


class Liquid(Status):
    status = "l"

    def __init__(self, temperature=super().temperature):
        self.temperature = temperature


class Solid(Status):
    status = "s"

    def __init__(self, temperature=super().temperature):
        self.temperature = temperature


class Aqua(Status):
    status = "aq"

    def __init__(self, temperature=super().temperature):
        self.temperature = temperature
