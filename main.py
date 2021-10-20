"""
Author: Ken Holm
Purpose: Introduce the numpy module
See: https://docs.scipy.org/doc/numpy/reference/index.html
"""

import numpy as np

def printAndHold(info, label ="", ask = False):
    if (label):
        print(label)

    print(info)

    if (ask):
        #input(f"Continue: ")
        print("==================================================")

    print()

rank1Array = np.array([1, 2, 3])
printAndHold(rank1Array, "Create a rank 1 array", True)

printAndHold(type(rank1Array[0]), "Create a rank 1 array", True)

printAndHold(type(rank1Array), "Print the type of rank1array", True)

printAndHold(rank1Array.shape, "Print the shape of rank1array", True)

printAndHold([rank1Array[0], rank1Array[1], rank1Array[2]], "Print each element of rank1array", True)

rank1Array[0] = 5
printAndHold(rank1Array, "Changing the element of the 0th element of rank1array", True)

printAndHold(np.random.choice(rank1Array), "Select a random item from this rank 1 array", False)
printAndHold(np.random.choice(rank1Array), "Select a random item from this rank 1 array", False)
printAndHold(np.random.choice(rank1Array), "Select a random item from this rank 1 array", True)

rank2Array = np.array([[1, 2, 3],
                       [4, 5, 6]])
printAndHold(rank2Array, "Create a two-dimensional/rank 2 array", True)

printAndHold(rank2Array.shape, "Print the shape of rank2array", True)

printAndHold([rank2Array[0, 0],
              rank2Array[0, 1],
              rank2Array[1, 0]], "Print specific elements of rank2array", True)

zerosArray = np.zeros((2, 2))
printAndHold(zerosArray, "Create a rank 2 array full of zeros", True)

printAndHold(type(zerosArray[0, 0]), "What is the data type for the created values?", True)

onesArray = np.ones((1, 2))
printAndHold(onesArray, "Create a rank 2 array full of ones", True)

constantArray = np.full((3, 2), 7)
printAndHold(constantArray, "Create a rank 2 array full of sevens", True)

printAndHold(type(constantArray[0, 0]), "Note the data type", True)

constantArray = np.full((3, 2), 7.)
printAndHold(constantArray, "Create a rank 2 array full of sevens", True)

printAndHold(type(constantArray[0, 0]), "Note the data type now", True)

randomArray = np.random.random((2, 2))
printAndHold(randomArray, "Create a rank 2 array full of random numbers", True)

randomArray = np.random.randint(1, 101, size=500)
printAndHold(randomArray, "Create array full of random integers between 1 and 100", True)

array3x4 = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12]])
printAndHold(array3x4.shape, "Shape of our 3x4 array", False)
printAndHold(array3x4, "Create a rank 2 array with a shape of 3 x 4", True)

# NOTE: Pulls first two rows, then columns 1 and 2
arraySlice = array3x4[:2, 1:3]
printAndHold(arraySlice, "Cut a slice from the array3x4 array", True)

printAndHold(arraySlice[0, 0], "Show arrayslice[0, 0]", True)

arraySlice[0, 0] = 100
printAndHold(arraySlice[0, 0], "Change arrayslice[0, 0] to 100", True)

longerArray =  np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9],
                         [10,  11,  12]])
printAndHold(longerArray, "A longer array of shape (4, 3)", True)

arrayOfIndices = np.array([0, 2, 0, 1])
printAndHold(arrayOfIndices, "Our array of indices", True)

printAndHold([longerArray[np.arange(4), arrayOfIndices]], "Picking out individual points from our array of indices", True)

longerArray[np.arange(4), arrayOfIndices] += 10
printAndHold(longerArray, "Adding 10 to specific points by our array of indices", True)

booleanIndex = (longerArray > 5)
printAndHold(booleanIndex, "Testing each point against our boolean index", True)

printAndHold(longerArray[booleanIndex], "Just show those points that pass our test", True)

shortList1 = np.array([[1, 2],
                       [3, 4]])
printAndHold(shortList1, "Short list #1", True)

shortList2 = np.array([[5, 6],
                       [7, 8]])
printAndHold(shortList2, "Short list #2", True)

printAndHold(shortList1 + shortList2, "Elementwise sum", True)

printAndHold(np.add(shortList1, shortList2), "Elementwise sum, TIMTOWTDI", True)

printAndHold(shortList1 - shortList2, "Elementwise difference", True)

printAndHold(np.subtract(shortList1, shortList2), "Elementwise difference, TIMTOWTDI", True)

printAndHold(shortList1 * shortList2, "Elementwise product", True)

printAndHold(np.multiply(shortList1, shortList2), "Elementwise product, TIMTOWTDI", True)

printAndHold(shortList1 / shortList2, "Elementwise division", True)

printAndHold(np.divide(shortList1, shortList2), "Elementwise division, TIMTOWTDI", True)

printAndHold(np.sqrt(shortList1), "Elementwise square root", True)

shortList3 = np.array([3, 5])
printAndHold(shortList3, "Short list #3", False)

shortList4 = np.array([7, 11])
printAndHold(shortList4, "Short list #4", True)

printAndHold(shortList3.dot(shortList4), "Product of vectors", False)
printAndHold(np.dot(shortList3, shortList4), "Product of vectors, TIMTOWTDI", True)

# Rank 1 array of matrix product
printAndHold(shortList1, "Reminder of short list #1", False)
printAndHold(shortList3, "Reminder of short list #3", False)
printAndHold(shortList1.dot(shortList3), "Rank 1 array of matrix/vector product", True)

# Rank 1 array of matrix product #2
printAndHold(shortList2, "Reminder of short list #2", False)
printAndHold(shortList4, "Reminder of short list #4", False)
printAndHold(np.dot(shortList2, shortList4), "Rank 1 array of matrix/vector product, TIMTOWTDI", True)

# Rank 2 array of matrix product
printAndHold(shortList1, "Reminder of short list #1", False)
printAndHold(shortList2, "Reminder of short list #2", False)
printAndHold(np.dot(shortList1, shortList2), "Rank 2 array of matrix/vector product", True)

# Sum columns
printAndHold(shortList1, "Reminder of short list #1", False)
printAndHold(np.sum(shortList1), "Sum of all elements", False)
printAndHold(np.sum(shortList1, axis=0), "Sum of all elements vertically", False)
printAndHold(np.sum(shortList1, axis=1), "Sum of all elements horizontally", True)

# Tons of mathematical functions
#  See https://docs.scipy.org/doc/numpy/reference/routines.math.html

printAndHold(shortList1, "Reminder of short list #1", False)
printAndHold(shortList1.T, "Transpose our array", True)

printAndHold(shortList3, "Reminder of short list #3", False)
printAndHold(shortList3.T, "Transposing a rank 1 array does nothing", True)

linSpaceArray = np.linspace(0, 1000, num=5, dtype=int)
printAndHold(linSpaceArray, "Created by .linspace()", True)

linSpaceArray = np.linspace(0, 1000, num=9, dtype=float)
printAndHold(linSpaceArray, "Created by .linspace()", True)



