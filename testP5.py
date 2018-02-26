#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 

import unittest
import p5Sergi

class test(unittest.TestCase):
	def test_cas1(self):
		#cas 1: llista amb un element [134]
		self.assertEqual(p5Sergi.aprobar([5,6,7,0,1,2]),[5,6,7,5,5,5])
	def test_cas2(self):
		self.assertEqual(p5Sergi.aprobar([]),[])
	def test_cas3(self):
		self.assertEqual(p5Sergi.aprobar([5,6,7,5,5,5]),[5,6,7,5,5,5])
	def test_cas4(self):
		self.assertEqual(p5Sergi.cercar([5,6,7,0,1,2],7),[2])
	def test_cas5(self):
		self.assertEqual(p5Sergi.cercar([5,6,7,0,1,2],8),[])
	def test_cas6(self):
		self.assertEqual(p5Sergi.cercar([5,6,7,7,1,2],7),[2,3])
	def test_cas7(self):
		self.assertEqual(p5Sergi.camviarNota([5,6,7,7,1,2],2,8),[5,6,8,7,1,2])
unittest.main()



