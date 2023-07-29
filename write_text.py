from lsb import image_text_utils
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

image_text_utils.write(INPUT_IMAGE, MESSAGE, OUTPUT)
