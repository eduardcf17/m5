#!/usr/bin/env python
# -*- coding: utf-8 -*-

def MostrarNota(notas):
	if len(notas)>0:
		for i in range (len(notas)):
			print notas[i],",",
	else:
		print"cap nota"
		
def AfegirNota(notas):
	print"Escriu la nota"
	nota=int(raw_input())
	notas.append(nota)
	return notas
def camviarNota(notas,posicion,notaNueva):
	"""
    Canvia les notes.
    >>> camviarNota ([5,6,7,0,1,2],2,8)
	[5, 6, 8, 0, 1, 2]
    """
	notas[posicion]=notaNueva
	return notas
	
def eliminar(notas):
	"""
    Retorna notas buides.
    >>> eliminar ([5,6,7,0,1,2])
    []
    """
	notas=[]
	return notas
	
def aprobar(notas):
	"""
    Retorna notas.
    >>> aprobar ([5,6,7,0,1,2])
    [5, 6, 7, 5, 5, 5]
    >>> aprobar ([5,6,7,5,5,5])
    [5, 6, 7, 5, 5, 5]
    >>> aprobar ([])
    []
    
    """
	for i in range (len(notas)):
		if notas[i]<5:
			notas[i]=5
	return notas
		 

def cercar(notas,notaBuscada):
	"""
    Cerca notes.
    >>> cercar ([5,6,7,0,1,2],7)
    [2]
    >>> cercar ([5,6,7,0,1,2],8)
    []
    >>> cercar ([5,6,7,7,1,2],7)
    [2, 3]
    """
	posicion=[]
	for i in range (len(notas)):
		if notas[i]==notaBuscada:
			posicion.append(i)
	return posicion

notas=[]


def interrogante():
	print"Escull una  de les seguents opcions opció"
	print"	m	Mostra les notes separades per coma segons l'exercici de llistes."
	print"	c   Canvia la nota de la posició p per n."
	print"	a	Afegeix una nova nota al final de a llista."
	print"	b	Buida les notes de la llista."
	print"	t	Aprova a tothom segons l'exercici de llistes."
	print"	d   «n»	Cerca la nota n i retorna la informació trobada segons l'exercici de llistes."
	print"	?	Mostra una ajuda amb un resum de les comandes disponibles."
	print"	x	Finalitza l'execució"

import doctest
doctest.testmod(verbose=True)
		
		
