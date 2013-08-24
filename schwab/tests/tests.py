#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import schwab
import unittest

USER_ID = os.getenv("USER_ID")
PASSWORD = os.getenv("PASSWORD")


class SimpleTestCase(unittest.TestCase):
	def test_simple(self):
		self.assertEqual(1 + 1, 2, "1+1 does not equal two.")

	def test_get_balance(self):
		schwab_browser = schwab.SchwabBrowser(USER_ID, PASSWORD)
		balance = schwab_browser.get_balance()
		self.assertEqual(type(balance), float, "Balance is not of type float.")


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout)
    logging.getLogger(__name__).setLevel(logging.DEBUG)
    unittest.main()
