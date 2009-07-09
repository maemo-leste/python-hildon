#!/usr/bin/env python2.5

import unittest
from sys import getrefcount

import hildon
import gtk

class TestHildonProgram(unittest.TestCase):
    def test_get_instance(self):
	hp = hildon.Program.get_instance()
	self.assertTrue(type(hp) is hildon.Program)

if __name__ == "__main__":
    unittest.main()
