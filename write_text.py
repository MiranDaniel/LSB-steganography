from lsb import write_text
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("src", help="Source location")
parser.add_argument("dest", help="Destination location")
parser.add_argument("msg", help="Message")
args = parser.parse_args()
config = vars(args)

INPUT_IMAGE = config["src"]
MESSAGE = config["msg"]
OUTPUT = config["dest"]

write_text.write(INPUT_IMAGE, MESSAGE, OUTPUT)
