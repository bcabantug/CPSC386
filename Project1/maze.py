#
import math
import sys
import random

#introduction
welcome = "Welcome to the maze generation. \n"
rowsA = input("Please input the amount of rows: ")
columnsA = input("Please input the amount of columns: ")

print (rowsA)
print (columnsA)

#variables 
#rowSize = (int(rowsA) * 2) + 1
#columnSize=(int(columnsA) * 2) +1
#print(rowSize)
#print(columnSize)

# global variables to print maze character 
#cornerChar = "+"
#horizontalChar = "-"
#verticalChar = "|"

#node class for the Binary space partition tree (eventually all leaves will be in order and will be able to draw out the maze)
class Node:
    #node constructor
    def __init__(self, beginHRange, endHRange, beginVRange, endVRange, left = none, right = none):
        self.coordinates = [[beginHRange,endHRange], [beginVRange,endVRange]]
        self.leftChild = left #left child 
        self.rightChild = right #right child

#recursive function to construct the BSP tree
def binarySP(rows, columns, currNode):
    
    #check if split still needs to happen (check if cell is already (total distance of 1 for height and width))
    if currNode.coordinates[0[1]]-currNode.coordinates[0[0]] == 1 && currNode.coordinates[1[1]]-currNode.coordinates[1[0]] == 1:
         #if current section is already part of the minimum size of cell 
         #then stop the split and return to previous parent node to continue the split
         return

    print currNode.coordinates

    else:
        selectRandSplit = randint(1,2)
        print selectRandSplit    #outputs the selected split direction

    

        #if split happens horizontally
        if selectRandSplit == 1:
            #get the random coordinate between the range of the current node to split betweeen for the children
            randSplit = randint(currNode.beginHRange, rows)
            #set the two nodes child nodes
            currNode.split1 = Node(currNode.coordinates[0[0]],randSplit,currNode.coordinates[1[0]] ,currNode.coordinates[1[1]])
            currNode.split2 = Node(randSplit+1, currNode.coordinates[0[1]],currNode.coordinates[1[0]] ,currNode.coordinates[1[1]])

            #start the recursive calls for the child nodes to develop the granchildren
            binarySP(currNode.split1.endHRange, currNode.split1.endVRange, currNode.split1)
            binarySP(currNode.split2.endHRange, currNode.split2.endVRange, currNode.split2)

        #if split happens vertically    
        elif selectRandSplit == 2:
            #get the random coordinate between the range of the current node to split between for the children
            randSplit = randint(currNode.beginVRange, columns)
             #set the two nodes child nodes
            currNode.split1 = Node(currNode.coordinates[0[0]],randSplit,currNode.coordinates[1[0]] ,currNode.coordinates[1[1]])
            currNode.split2 = Node(randSplit+1, currNode.coordinates[0[1]],currNode.coordinates[1[0]] ,currNode.coordinates[1[1]])

            #start the recursive calls for generating the next child nodes
            binarySP(currNode.split1.endHRange, currNode.split1.endVRange, currNode.split1)
            binarySP(currNode.split2.endHRange, currNode.split2.endVRange, currNode.split2)



treeRoot = Node(0, int(rowsA), 0, int(columnsA),none, none)

binarySP(int(rowsA), int(columnsA), treeRoot)

#beginSpace = Node(int(rowsA), int(columnsA)