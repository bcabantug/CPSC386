#
import math
import sys
import random

welcome = "Welcome to the maze generation. \n"
rowsA = input("Please input the amount of rows: ")
columnsA = input("Please input the amount of columns: ")

print (rowsA)
print (columnsA)



#variables 
rowSize = (int(rowsA) * 2) + 1
columnSize=(int(columnsA) * 2) +1



print(rowSize)
print(columnSize)
#variables to print how 
cornerChar = "+"
horizontalChar = "-"
verticalChar = "|"

#node class for the Binary space partition tree
#class node:
#    
#    def __init__(self, hRange, vRange):
#        self.coordinates = [[0,hRange], [0,vRange]]
#        self.split1 = none
#        self.split2 = none

#def binarySP(rowsA, columnsA):


