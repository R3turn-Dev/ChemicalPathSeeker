#
# Parser
# Author: Eunhak Lee(@return0927)
#
import re
import logging
import traceback
from .status import Gas, Liquid, Solid, Aqua
from .prototype import Atom, Compound, Equation, ThermochemicalEquation
from .exception import ChemException, ParseError


class Parser:
    def __init__(self):
        self.status = 0
        self.algorithm = [
            self.separate_compounds
            ]

    def run(self, data):
        self.status = 1

        try:
            for func in self.algorithm:
                data = func(data)

            self.status = 0
            return data

        except ChemException as ex:
            self.status = -1

            return ex

    @classmethod
    def separate_compounds(cls, data):
        """

        :param data: string of compounds or an equation
        :return: Compound or Equation
        """
        # Equation mode
        if "->" in data:
            before, after = data.split("->")
            before = [x.strip() for x in before.split("+")]
            after = [x.strip() for x in after.split("+")]

            before = [cls.parse_compound(compound) for compound in before]
            after = [cls.parse_compound(compound) for compound in after]

            return Equation(before_compounds=before, after_compounds=after)

        # Compounds mode
        else:
            compounds = [x.strip() for x in data.split("+")]
            parsed_compounds = []

            for compound in compounds:
                try:
                    parsed = cls.parse_compound(compound)
                    parsed_compounds.append(parsed)
                except ParseError as ex:
                    logging.warning(f"Error occured when parsing compound `{compound}`\n" +
                                    "\n".join(
                                        "\t" + x for x in traceback.format_exc()
                                        )
                                    )
                    parsed_compounds.append(ex)

            return parsed_compounds

    @classmethod
    def parse_compound(cls, data):
        """Convert compound string into compound class

        :param data: string of a compound
        :return: class Chem.prototype.Compound
        """
        prefix_count = 1

        # Starting with count of compound
        if data[0].isnumeric():
            prefix_count = int(data[0])
            data = data[1:]

        compound = data
        status = "(g)"
        # If indicating status or sth else
        if ("(" in compound and ")" in compound) and \
                0 <= compound.index("(") < compound.index(")") < len(compound):
            compound, status = compound[:compound.index("(")], compound[compound.index("("):]

        # Parse status with Parser.parse_status
        status = cls.parse_status(status)

        found_atoms = re.compile(r"([A-Z][a-z]*)(\d*)").findall(compound)
        atoms = []

        for atom, count in found_atoms:
            count = int(count) if count.isnumeric() else 1
            for n in range(int(count)):
                atoms.append(Atom.derive_from_atomic_repr(atom))

        return Compound(
            atoms,
            count=prefix_count,
            status=status
            )

    @classmethod
    def parse_status(cls, data):
        """Convert () stripped string into status and meta information

        :param data: () stripped string
        :return: parsed data as Chem.status.Status
        """
        if not (data[0] == "(" and data[-1] == ")"):
            raise ParseError("Unexpected status string passed", data=data)

        sections = [x.strip() for x in data[1:-1].split(",")]
        status = Gas
        metas = []
        temperature = -1
        for section in sections:
            # If specified status of compound
            if section.lower() in ("g", "l", "s", "aq"):
                proxy = [
                    Gas,
                    Liquid,
                    Solid,
                    Aqua
                    ]

                status = proxy[("g", "l", "s", "aq").index(section)]

            # If specified temperature of compound
            elif re.compile(r"^\d+[k℃]$").match(section.lower()):
                if temperature >= 0:
                    raise ParseError("Temperature was specified multiple times in meta information", data=data)
                temp, unit = int(section[:-1]), section[-1].lower()

                temperature = temp + (0 if unit == "k" else 273)
            else:
                metas.append(section)

        return status(
            temp=273 if temperature < 0 else temperature,
            meta=", ".join(metas)
            )
