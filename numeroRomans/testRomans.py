#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import unittest
import numerosRomans
class test(unittest.TestCase):
	def test_cas1(self):
		self.assertEqual(numerosRomans.romans(1),'I')	
	def test_cas2(self):
		self.assertEqual(numerosRomans.romans(2),'II')	
	def test_cas3(self):
		self.assertEqual(numerosRomans.romans(3),'III')	
	
unittest.main()
