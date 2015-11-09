# -*- coding: utf-8 -*-

import unittest
from tests import TestCalculator

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    unittest.main()
