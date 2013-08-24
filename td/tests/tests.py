#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import unittest

logger = logging.getLogger(__name__)
logging.basicConfig(level='ERROR')


class SimpleTestCase(unittest.TestCase):
	def test_simple(self):
		self.assertEqual(1 + 1, 2, "1+1 does not equal two.")

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout)
    logging.getLogger(__name__).setLevel(logging.DEBUG)
    unittest.main()
