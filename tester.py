import logging
import traceback
from Chem.parser import Parser
from Chem.exception import ParseError
from Chem.grouper import Grouper

logging.basicConfig(level=logging.DEBUG)


# Read cases from case.txt
cases = open("Case.txt", encoding="UTF-8").read().split("\n")
logging.info(f"Read {len(cases)} cases.")
"""
for case in cases:
    parser = Parser()
    try:
        print(f" > Testing case: {case }")
        data = parser.run(case)
        print(f" < {repr(data)}")
        print()
    except ParseError as ex:
        print(ex.data)
        traceback.print_exc()
        raise ex
"""

# test Grouper
cases = cases[5:]
grouper = Grouper()

for case in cases:
    grouper.add_equation(case)

[print(x) for x in grouper.estimate()]
"""
print("Cases", cases)

first = Parser().run(cases[0])
second = Parser().run(cases[1])

print("First -", first)
print("Reverse -", first.reverse())
print("Second -", second)
print("Reverse -", second.reverse())
print("Add -", first + second)
print("Sub -", first - second)
"""