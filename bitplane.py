from lsb import bitplane

import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("src", help="Source location")

args = parser.parse_args()
config = vars(args)

bitplane.analyze(config["src"]).show()
