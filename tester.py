import logging

logging.basicConfig(level=logging.DEBUG)


# Read cases from case.txt
cases = open("Case.txt").readlines()
logging.info(f"Read {len(cases)} cases.")

