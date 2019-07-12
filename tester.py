import logging
import traceback
from Chem.parser import Parser
from Chem.exception import ParseError

logging.basicConfig(level=logging.DEBUG)


# Read cases from case.txt
cases = open("Case.txt", encoding="UTF-8").read().split("\n")
logging.info(f"Read {len(cases)} cases.")

for case in cases:
    parser = Parser()
    try:
        print(f" > {case }")
        data = parser.parse_compound(case)
        print(f" < {data}")
    except ParseError as ex:
        print(ex.data)
        traceback.print_exc()
        raise ex
