#
# Chem.status
# Author: Eunhak Lee(@return0927)
#


class Status:
    status = ""

    def __str__(self):
        data = ", ".join(x for x in [
                self.status,
                self.temperature if self.temperature != 273.0 else "",
                self.meta
                ] if x
            )
        return "{}".format("(" + data + ")" if data else "")

    def __init__(self, meta: str = "", temp: float = 273):
        self.temperature = temp
        self.meta = meta


class Gas(Status):
    status = "g"


class Liquid(Status):
    status = "l"


class Solid(Status):
    status = "s"


class Aqua(Status):
    status = "aq"
