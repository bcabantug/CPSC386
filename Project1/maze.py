#
import math
import sys
import random

#introduction
welcome = "Welcome to the maze generation. \n"
rowsA = input("Please input the amount of rows: ")
columnsA = input("Please input the amount of columns: ")

#takes the input and multiplies it by two to get the full range of the maze to calculate
rowsI = int(rowsA*2)
columnsI = int(columnsA*2)

#variable to hold coordinates for portals when generating maze
mazePortals = []

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
    def __init__(self, beginHRange, endHRange, beginVRange, endVRange, left=None, right=None):
        self.coordinates = [[beginHRange,endHRange], [beginVRange,endVRange]]
        self.leftChild = left #left child 
        self.rightChild = right #right child



#recursive function to construct the BSP tree
def binarySP(rows, columns, currNode):
    
    print(currNode.coordinates)

    #check if split still needs to happen (check if cell is already (total distance of 1 for height and width))
    #if currNode.coordinates[0][1]-currNode.coordinates[0][0] == 2 or currNode.coordinates[1][1]-currNode.coordinates[1][0] == 2:
         #if current section is already part of the minimum size of cell 
         #then stop the split and return to previous parent node to continue the split
         #print("Returning to previous node due to no more splits")
    #     return None

    #print(currNode.coordinates)

    #else:
    

    
    selectRandSplit = random.randint(1,2)
    print (str(selectRandSplit) + "\n\n")    #outputs the selected split direction

    #if split happens horizontally
    if selectRandSplit == 1:
       #get the random coordinate between the range of the current node to split betweeen for the children            
            
       #if there is only one possible split between the current section (cell length = 4)
       if currNode.coordinates[0][1]-currNode.coordinates[0][0] == 4:
            #set it so that the split is equivalent of to have the cell coordinate be size 1
            currNode.split1=Node(currNode.coordinates[0][0], currNode.coordinates[0][0]+2, currNode.coordinates[1][0], currNode.coordinates[1][1])
            print(currNode.split1.coordinates)
            currNode.split2=Node(currNode.coordinates[0][0]+2, currNode.coordinates[0][1], currNode.coordinates[1][0], currNode.coordinates[1][1])
            print(currNode.split2.coordinates)
            
        else:

            randSplit = random.randrange(currNode.coordinates[0][0], currNode[0][1],2)
        
            #adjust split for situation where a number is picked such that it is equal to the last edge of the rows
            #if randSplit+1 == currNode.coordinates[0][1] or randSplit == currNode.coordinates[0][0]:
            #    randSplit = random.randint(currNode.coordinates[0][0]+1, rows-1) #untested condition

            

            print("rand "+str(randSplit) + "\n") #outputs the coordinate that will be split among them
                #set the two nodes child nodes
            
            
            currNode.split1 = Node(currNode.coordinates[0][0],randSplit,currNode.coordinates[1][0] ,currNode.coordinates[1][1])
            print(currNode.split1.coordinates)
            currNode.split2 = Node(randSplit, currNode.coordinates[0][1],currNode.coordinates[1][0] ,currNode.coordinates[1][1])
            print(currNode.split2.coordinates)

            #start the recursive calls for the child nodes to develop the granchildren
            print ("split1RandH")
            binarySP(currNode.split1.coordinates[0][1], currNode.split1.coordinates[1][1], currNode.split1)
            print ("split2RandH")
            binarySP(currNode.split2.coordinates[0][1], currNode.split2.coordinates[1][1], currNode.split2)

        #if split happens vertically    
    elif selectRandSplit == 2:

            #if there is only one possible split between the current section (cell length = 2)
        if currNode.coordinates[1][1]-currNode.coordinates[1][0] == 4:
            #set it so that the split is equivalent of to have the cell coordinate be size 1
            currNode.split1=Node(currNode.coordinates[0][0], currNode.coordinates[0][1], currNode.coordinates[1][0], currNode.coordinates[1][0]+2)
            print(currNode.split1.coordinates)
            currNode.split2=Node(currNode.coordinates[0][0], currNode.coordinates[0][1], currNode.coordinates[1][0]+2, currNode.coordinates[1][1])
            print(currNode.split2.coordinates)
            
        else:
                #get the random coordinate between the range of the current node to split between for the children
            randSplit = random.randrange(currNode.coordinates[1][0], currNode[1]][1],2)

            print("rand "+str(randSplit) + "\n")

            
                #currNode.split1 = Node(currNode.coordinates[0][0],randSplit,currNode.coordinates[1][0] ,currNode.coordinates[1][1])
                #currNode.split2 = Node(randSplit+1, currNode.coordinates[0][1],currNode.coordinates[1][0] ,currNode.coordinates[1][1])
            currNode.split1 = Node(currNode.coordinates[0][0], currNode.coordinates[0][1],currNode.coordinates[1][0] ,randSplit)
            print(currNode.split1.coordinates)

            currNode.split2 = Node(currNode.coordinates[0][0], currNode.coordinates[0][1],randSplit,currNode.coordinates[1][1])
            print(currNode.split2.coordinates)

            #start the recursive calls for generating the next child nodes
        print ("split1RandV")
        binarySP(currNode.split1.coordinates[0][1], currNode.split1.coordinates[1][1], currNode.split1)
        print ("split2RandV")
        binarySP(currNode.split2.coordinates[0][1], currNode.split2.coordinates[1][1], currNode.split2)



treeRoot = Node(0, rowsI, 0, columnsI)

binarySP(rowsI, columnsI, treeRoot)

#beginSpace = Node(int(rowsA), int(columnsA)