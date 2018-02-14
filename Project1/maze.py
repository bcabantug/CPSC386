#
import math
import sys
import random

#introduction
welcome = "Welcome to the maze generation. \n"
rowsA = input("Please input the amount of rows: ")
columnsA = input("Please input the amount of columns: ")

#takes the input and multiplies it by two to get the full range of the maze to calculate
rowsI = int(rowsA)*2
columnsI = int(columnsA)*2

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
        self.split1 = left #left child 
        self.split2 = right #right child

    #function to append child nodes to current Node
    #def append(self, splitNum, childNode):
    #    self.split+str(splitNum) = childNode



#recursive function to construct the BSP tree
def binarySP(rows, columns, currNode):
    
    print("currCoordinates:")
    print(currNode.coordinates)
    

    
    selectRandSplit = random.randint(1,2)
    print (str(selectRandSplit) + "\n\n")    #outputs the selected split direction

    #if split happens horizontally
    if selectRandSplit == 1:
       #get the random coordinate between the range of the current node to split betweeen for the children            
       horizontalSplit(currNode)     
       ''' #if there is only one possible split between the current section (cell length = 4)
        if currNode.coordinates[0][1]-currNode.coordinates[0][0] == 4:
            print("final split for this direction-section")
            #set it so that the split is equivalent of to have the cell coordinate be size 2
            currNode.split1=Node(currNode.coordinates[0][0], currNode.coordinates[0][0]+2, currNode.coordinates[1][0], currNode.coordinates[1][1])
            print(currNode.split1.coordinates)
            currNode.split2=Node(currNode.coordinates[0][0]+2, currNode.coordinates[0][1], currNode.coordinates[1][0], currNode.coordinates[1][1])
            print(currNode.split2.coordinates)

        #if the split selected causes it to split on itself
        elif currNode.coordinates[0][1]-currNode.coordinates[0][0]==2:
            #check if the current node still has range to split for opposite direction
            if currNode.coordinates[1][1] - currNode[1][0] != 2:
                #call split function to split opposite direction for region


            
            
        #covers final case where cell can no longer be split upon itself
        elif currNode.coordinates[0][1]-currNode.coordinates[0][0]==2 and currNode.coordinates[1][1]-currNode.coordinates[1][0]==2:
            #then stop the split and return to previous parent node to continue the split function
            print("Returning to previous node due to no more possible splits")

        
        else:
            #check to make sure that origin line coordinate ranges are not selected for the split (ex: [0][0])
            tmpLower = 2
            if(currNode.coordinates[0][0]!=0):
                tmpLower = currNode.coordinates[0][0]


            randSplit = random.randrange(tmpLower, currNode.coordinates[0][1],2)
        
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
            binarySP(currNode.split2.coordinates[0][1], currNode.split2.coordinates[1][1], currNode.split2) '''

    #if split happens vertically    
    elif selectRandSplit == 2:
        verticalSplit(currNode)
        '''  #if there is only one possible split between the current section (cell length = 2)
        if currNode.coordinates[1][1]-currNode.coordinates[1][0] == 4:
            print("final split")
            #set it so that the split is equivalent of to have the cell coordinate be size 1
            currNode.split1=Node(currNode.coordinates[0][0], currNode.coordinates[0][1], currNode.coordinates[1][0], currNode.coordinates[1][0]+2)
            print(currNode.split1.coordinates)
            currNode.split2=Node(currNode.coordinates[0][0], currNode.coordinates[0][1], currNode.coordinates[1][0]+2, currNode.coordinates[1][1])
            print(currNode.split2.coordinates)
        
        elif currNode.coordinates[1][1]-currNode.coordinates[1][0] == 2:
             #if current section is already part of the minimum size of cell 
            #then stop the split and return to previous parent node to continue the split
            print("Returning to previous node due to no more possible splits")

            
        else:

            #check to make sure that origin line coordinate ranges are not selected for the split (ex: [0][0])
            tmpLower = 2
            if(currNode.coordinates[1][0]!=0):
                tmpLower = currNode.coordinates[1][0]
            
            #get the random coordinate between the range of the current node to split between for the children
            randSplit = random.randrange(tmpLower, currNode.coordinates[1][1],2)

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
            binarySP(currNode.split2.coordinates[0][1], currNode.split2.coordinates[1][1], currNode.split2) '''


#function to define horizontal split
def horizontalSplit(nodeToSplit):
    #get the random coordinate between the range of the current node to split betweeen for the children            
            
    #if there is only one possible split between the current section (cell length = 4)
    if nodeToSplit.coordinates[0][1]-nodeToSplit.coordinates[0][0] == 4:
        print("final split for this direction-section")
        #set it so that the split is equivalent of to have the cell coordinate be size 2
        nodeToSplit.split1=Node(nodeToSplit.coordinates[0][0], nodeToSplit.coordinates[0][0]+2, nodeToSplit.coordinates[1][0], nodeToSplit.coordinates[1][1])
        print(nodeToSplit.split1.coordinates)
        nodeToSplit.split2=Node(nodeToSplit.coordinates[0][0]+2, nodeToSplit.coordinates[0][1], nodeToSplit.coordinates[1][0], nodeToSplit.coordinates[1][1])
        print(nodeToSplit.split2.coordinates)

         #start the recursive calls for the child nodes to develop the granchildren
        print ("split1RandH")
        binarySP(nodeToSplit.split1.coordinates[0][1], nodeToSplit.split1.coordinates[1][1], nodeToSplit.split1)
        print ("split2RandH")
        binarySP(nodeToSplit.split2.coordinates[0][1], nodeToSplit.split2.coordinates[1][1], nodeToSplit.split2)



        #if the split selected causes it to split on itself
    elif nodeToSplit.coordinates[0][1]-nodeToSplit.coordinates[0][0]==2:
        #check if the current node still has range to split for opposite direction
        if nodeToSplit.coordinates[1][1] - nodeToSplit.coordinates[1][0] != 2:
            #call split function to split opposite direction for region
            verticalSplit(nodeToSplit)


            
            
    #covers final case where cell can no longer be split upon itself
    elif nodeToSplit.coordinates[0][1]-nodeToSplit.coordinates[0][0]==2 and nodeToSplit.coordinates[1][1]-nodeToSplit.coordinates[1][0]==2:
        #then stop the split and return to previous parent node to continue the split function
        print("Returning to previous node due to no more possible splits")

        
    else:
        #check to make sure that origin line coordinate ranges are not selected for the split (ex: [0][0])
        tmpLower = 2
        if(nodeToSplit.coordinates[0][0]!=0):
            tmpLower = nodeToSplit.coordinates[0][0]


        randSplit = random.randrange(tmpLower, nodeToSplit.coordinates[0][1],2)
        while randSplit == tmpLower:
            randSplit = random.randrange(tmpLower, nodeToSplit.coordinates[0][1],2)
        
        #adjust split for situation where a number is picked such that it is equal to the last edge of the rows
        #if randSplit+1 == currNode.coordinates[0][1] or randSplit == currNode.coordinates[0][0]:
        #    randSplit = random.randint(currNode.coordinates[0][0]+1, rows-1) #untested condition

            

        print("rand "+str(randSplit) + "\n") #outputs the coordinate that will be split among them
        #set the two nodes child nodes
            
            
        nodeToSplit.split1 = Node(nodeToSplit.coordinates[0][0],randSplit,nodeToSplit.coordinates[1][0] ,nodeToSplit.coordinates[1][1])
        print(nodeToSplit.split1.coordinates)
        nodeToSplit.split2 = Node(randSplit, nodeToSplit.coordinates[0][1],nodeToSplit.coordinates[1][0] ,nodeToSplit.coordinates[1][1])
        print(nodeToSplit.split2.coordinates)

        #start the recursive calls for the child nodes to develop the granchildren
        print ("split1RandH")
        binarySP(nodeToSplit.split1.coordinates[0][1], nodeToSplit.split1.coordinates[1][1], nodeToSplit.split1)
        print ("split2RandH")
        binarySP(nodeToSplit.split2.coordinates[0][1], nodeToSplit.split2.coordinates[1][1], nodeToSplit.split2)


#function to define vertical split
def verticalSplit(nodeToSplit):
    #if there is only one possible split between the current section (cell length = 2)
    if nodeToSplit.coordinates[1][1]-nodeToSplit.coordinates[1][0] == 4:
        print("final split")
        #set it so that the split is equivalent of to have the cell coordinate be size 1
        nodeToSplit.split1=Node(nodeToSplit.coordinates[0][0], nodeToSplit.coordinates[0][1], nodeToSplit.coordinates[1][0], nodeToSplit.coordinates[1][0]+2)
        print(nodeToSplit.split1.coordinates)
        nodeToSplit.split2=Node(nodeToSplit.coordinates[0][0], nodeToSplit.coordinates[0][1], nodeToSplit.coordinates[1][0]+2, nodeToSplit.coordinates[1][1])
        print(nodeToSplit.split2.coordinates)

        #start the recursive calls for generating the next child nodes
        print ("split1RandV")
        binarySP(nodeToSplit.split1.coordinates[0][1], nodeToSplit.split1.coordinates[1][1], nodeToSplit.split1)
        print ("split2RandV")
        binarySP(nodeToSplit.split2.coordinates[0][1], nodeToSplit.split2.coordinates[1][1], nodeToSplit.split2)

    #if the split selected causes it to split on itself
    elif nodeToSplit.coordinates[1][1]-nodeToSplit.coordinates[1][0]==2:
        #check if the current node still has range to split for opposite direction
        if nodeToSplit.coordinates[0][1] - nodeToSplit.coordinates[0][0] != 2:
            #call split function to split opposite direction for region
            horizontalSplit(nodeToSplit)




    elif nodeToSplit.coordinates[1][1]-nodeToSplit.coordinates[1][0] == 2:
         #if current section is already part of the minimum size of cell 
        #then stop the split and return to previous parent node to continue the split
        print("Returning to previous node due to no more possible splits")

            
    else:

        #check to make sure that origin line coordinate ranges are not selected for the split (ex: [0][0])
        tmpLower = 2
        if(nodeToSplit.coordinates[1][0]!=0):
            tmpLower = nodeToSplit.coordinates[1][0]
            
        #get the random coordinate between the range of the current node to split between for the children
        
        randSplit = random.randrange(tmpLower, nodeToSplit.coordinates[1][1],2)
            #check to make sure the lower boundary is not selected as the split and repick split if it is selected
        while randSplit == tmpLower:
            randSplit = random.randrange(tmpLower, nodeToSplit.coordinates[1][1],2)
        
        print("rand "+str(randSplit) + "\n")

            
            #currNode.split1 = Node(currNode.coordinates[0][0],randSplit,currNode.coordinates[1][0] ,currNode.coordinates[1][1])
            #currNode.split2 = Node(randSplit+1, currNode.coordinates[0][1],currNode.coordinates[1][0] ,currNode.coordinates[1][1])
        nodeToSplit.split1 = Node(nodeToSplit.coordinates[0][0], nodeToSplit.coordinates[0][1],nodeToSplit.coordinates[1][0] ,randSplit)
        print(nodeToSplit.split1.coordinates)

        nodeToSplit.split2 = Node(nodeToSplit.coordinates[0][0], nodeToSplit.coordinates[0][1],randSplit,nodeToSplit.coordinates[1][1])
        print(nodeToSplit.split2.coordinates)

        #start the recursive calls for generating the next child nodes
        print ("split1RandV")
        binarySP(nodeToSplit.split1.coordinates[0][1], nodeToSplit.split1.coordinates[1][1], nodeToSplit.split1)
        print ("split2RandV")
        binarySP(nodeToSplit.split2.coordinates[0][1], nodeToSplit.split2.coordinates[1][1], nodeToSplit.split2)



#function to print out tree leaves to verify all splits are correct
def printTreeLeaves(cNode):
    if cNode == None:
        print ("")
    else:
        if cNode.split1 == None and cNode.split2==None:
            print(cNode.coordinates)
       
        printTreeLeaves(cNode.split1)
        
        printTreeLeaves(cNode.split2)



treeRoot = Node(0, rowsI, 0, columnsI)

binarySP(rowsI, columnsI, treeRoot)


print("Printing leaves of bspTree:")
printTreeLeaves(treeRoot)

#beginSpace = Node(int(rowsA), int(columnsA)