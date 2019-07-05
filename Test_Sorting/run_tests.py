import os
import importlib
from test.sorting_algorithm_tests import run_tests



if __name__ == '__main__':

    module_names = [module_name[:-3] for module_name in os.listdir('sorting_algorithms') if module_name[-7:] == 'sort.py']
    sorting_functions = [importlib.import_module("sorting_algorithms.{}".format(module)).sort_method for module in module_names]

    for name, failure in run_tests(sorting_functions, module_names):
        if failure:
            print('Sorting algorithm {} failed in test {} \n'.format(name, str(failure)))