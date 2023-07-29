from lsb import read_text
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("src", help="Source location")
parser.add_argument(
    "--startbit", "-s", help="Start bit plane", default=0, required=False
)
parser.add_argument("--endbit", "-e", help="End bit plane", default=0, required=False)
args = parser.parse_args()
config = vars(args)

INPUT_IMAGE = config["src"]
START_BIT = int(config["startbit"])
END_BIT = int(config["endbit"])

text = read_text.read(INPUT_IMAGE, START_BIT, END_BIT)
print(text)
