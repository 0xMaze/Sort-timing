import random


class ArrayGenerator:
    def __init__(self):
        self.small_random_array = self.generate_small_random_array()
        self.small_sorted_array = self.generate_small_sorted_array()
        self.small_reversed_array = self.generate_small_reversed_array()

        self.big_random_array = self.generate_big_random_array()
        self.big_sorted_array = self.generate_big_sorted_array()
        self.big_reversed_array = self.generate_big_reversed_array()

    def generate_small_random_array(self):
        """Generate a small random array of numbers"""

        return [random.randint(0, 100) for _ in range(10)]

    def generate_small_sorted_array(self):
        """Generate a small sorted array of numbers"""
        return sorted(self.generate_small_random_array())

    def generate_small_reversed_array(self):
        """Generate a small reversed array of numbers"""
        return sorted(self.generate_small_random_array(), reverse=True)

    def generate_big_random_array(self):
        """Generate a big random array of numbers"""

        return [random.randint(0, 100) for _ in range(1000)]

    def generate_big_sorted_array(self):
        """Generate a big sorted array of numbers"""
        return sorted(self.generate_big_random_array())

    def generate_big_reversed_array(self):
        """Generate a big reversed array of numbers"""
        return sorted(self.generate_big_random_array(), reverse=True)
