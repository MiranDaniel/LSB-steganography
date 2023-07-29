import unittest
from enum import Enum
import lsb
import numpy as np
import os.path
from PIL import Image

class TestImage(Enum):
    CAT = "./sample_images/cat.png"
    LICHTENSEIN = "./sample_images/lichtenstein.png"
    TREES = "./sample_images/trees.png"
    NOT_EXIST = "./sample_images/invalid"


class TestSum(unittest.TestCase):
    def test_bitplane_analyzer_plot(self):
        result = lsb.bitplane.analyze(TestImage.CAT.value)
        assert type(result) is np.ndarray

    def test_bitplane_analyzer_savefig(self):
        for i in {TestImage.CAT, TestImage.LICHTENSEIN, TestImage.TREES}:
            lsb.bitplane.analyze(i.value)
            assert os.path.isfile("./output/bitplanes.png")
            im = Image.open("./output/bitplanes.png")
            im.verify()

    def test_bitplane_analyzer_invalid_file(self):
        try:
            lsb.bitplane.analyze(TestImage.NOT_EXIST.value)
        except FileNotFoundError:
            return

    def test_combine_bitplanes(self):
        files = {"red","green","blue","combined"}
        for i in (True, False):
            for j in (True, False):
                for upper in range(0,7):
                    lsb.bitplane.combine(TestImage.CAT.value, 0, upper, i, j, "./output/")
                    for i in files:
                        assert os.path.isfile(f"./output/secret_{i}.png")
                        im = Image.open(f"./output/secret_{i}.png")
                        im.verify()

    def test_combine_bitplanes_invalid_file(self):
        try:
            lsb.bitplane.analyze(TestImage.NOT_EXIST.value)
        except FileNotFoundError:
            return

    def test_combine_bitplanes_invalid_range(self):
        try:
            lsb.bitplane.combine(TestImage.CAT.value, 0, 16, True, False, "./output/")
        except IndexError:
            ...
        try:
            lsb.bitplane.combine(TestImage.CAT.value, 8, 6, True, False, "./output/")
        except Warning:
            ...



if __name__ == "__main__":
    unittest.main()
