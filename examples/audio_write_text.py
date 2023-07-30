import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from lsb import audio
import argparse


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("src", help="Source location")
parser.add_argument("dest", help="Destination location")
parser.add_argument("msg", help="Message")
args = parser.parse_args()
config = vars(args)

INPUT_AUDIO = config["src"]
MESSAGE = config["msg"]
OUTPUT = config["dest"]

audio.text.write(
    INPUT_AUDIO, MESSAGE, OUTPUT
)
