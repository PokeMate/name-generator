import unittest
import os
from generator import NameGenerator, load_names


class TestGenerator(unittest.TestCase):
    model_path = os.path.realpath("./api/static/model.h5")
    input_names_path = os.path.realpath("./api/static/names.txt")
    generator = NameGenerator(model_path, input_names_path)

    def test_names_path(self):
        path = os.path.realpath("./api/static/names.txt")
        names = load_names(path)

        # if names not empty, the file was successfully loaded
        self.assertGreater(len(names), 0)

    def test_broken_names_path(self):
        with self.assertRaises(FileNotFoundError):
            load_names("./brokenPath")

    def test_name_length(self):
        amount = 1
        new_names = self.generator.generate_names(amount)
        self.assertEqual(len(new_names), amount)

    def test_name_length_below_lowerbound(self):
        amount = 0
        with self.assertRaises(Exception):
            self.generator.generate_names(amount)

    def test_name_length_above_upperbound(self):
        amount = 11
        with self.assertRaises(Exception):
            self.generator.generate_names(amount)

    def test_name_length_string_input(self):
        amount = "string input"
        with self.assertRaises(Exception):
            self.generator.generate_names(amount)


if __name__ == "__main__":
    unittest.main()
