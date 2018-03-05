#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
def romans(numero):
	NumeroRoma=''
	if numero <=3:
		for i in range(0,numero):
			NumeroRoma+= "I"
	else:
		NumeroRoma="V"
	for i in range(0,numero):
		NumeroRoma+= "I"
		
	return NumeroRoma
