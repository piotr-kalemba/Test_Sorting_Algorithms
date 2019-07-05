import unittest
import random
from unittest import TestLoader

class TestParameterizedTestcase(unittest.TestCase):

    sorting_algorithm = None
    module_name = None

    @classmethod
    def setUpClass(cls):

        print('Sorting algorithm: {}\n'.format(cls.module_name))

    def test_empty_list(self):

        resulting_list = self.__class__.sorting_algorithm([])
        self.assertListEqual([], resulting_list)

    def test_one_element_list(self):

        resulting_list = self.__class__.sorting_algorithm([1])
        self.assertListEqual([1], resulting_list)


    def test_two_element_list(self):

        resulting_list = self.__class__.sorting_algorithm([2, 1])
        self.assertListEqual([1, 2], resulting_list)

    def test_long_list(self):

        elements = list(range(100))
        random_list = random.choices(elements, k=50)
        sorted_list = sorted(random_list)
        resulting_list = self.__class__.sorting_algorithm(random_list)
        self.assertListEqual(resulting_list, sorted_list)


def run_tests(algorithms, module_names):

    results = []

    for module_name, sorting_algorithm in zip(module_names, algorithms):

        suite = unittest.TestSuite()
        loader = TestLoader()
        TestParameterizedTestcase.sorting_algorithm = sorting_algorithm
        TestParameterizedTestcase.module_name = module_name
        tests = loader.loadTestsFromTestCase(TestParameterizedTestcase)
        suite.addTest(tests)
        r = unittest.TextTestRunner().run(suite)
        results.append((module_name, r.failures))

    return results