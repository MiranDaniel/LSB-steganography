import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from lsb import audio
import argparse


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("src", help="Source location")

args = parser.parse_args()
config = vars(args)

audio.bitplane.analyze(config["src"])
