from lsb import combine_bitplanes
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("src", help="Source location")
parser.add_argument(
    "--out", "-o", help="Output location", default="./output/", required=False
)
parser.add_argument(
    "--startbit", "-s", help="Start bit plane", default=0, required=False
)
parser.add_argument("--endbit", "-e", help="End bit plane", default=0, required=False)
parser.add_argument(
    "--color", "-c", help="Use color for the result", default=False, required=False
)
parser.add_argument(
    "--saveall", "-a", help="Save all bit planes", default=False, required=False
)
args = parser.parse_args()
config = vars(args)

INPUT_IMAGE = config["src"]
START_BIT = int(config["startbit"])
END_BIT = int(config["endbit"])
SAVE_EACH_BIT = config["saveall"]
COLOR = config["color"]

OUTPUT_DIR = config["out"]

combine_bitplanes.run(INPUT_IMAGE, START_BIT, END_BIT, SAVE_EACH_BIT, COLOR, OUTPUT_DIR)
