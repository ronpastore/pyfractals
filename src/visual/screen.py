from config import MATRIX_SIZE

'''
Created on 11 Nov 2010

@author: Ron Pastore
'''
from matrix.cell import cell

class screen:

    def __init__(self):
        matrix_range = range(1,MATRIX_SIZE)
        self.matrix = [ [ cell(x,y) for x in matrix_range] for y in matrix_range]

