"""
Author: Ken Holm
Purpose: Introduce the numpy module
See: https://docs.scipy.org/doc/numpy/reference/index.html
"""

import numpy as np

def hold(info, label = "", ask = False):
    if (label):
        print(label)

    print(info)

    if (ask):
        input(f"Continue: ")
        print("==================================================")

    print()

rank1array = np.array([1, 2, 3])
hold(rank1array, "Create a rank 1 array", True)

hold(type(rank1array), "Print the type of rank1array", True)

hold(rank1array.shape, "Print the shape of rank1array", True)

hold([rank1array[0], rank1array[1], rank1array[2]], "Print each element of rank1array", True)

rank1array[0] = 5
hold(rank1array, "Changing the element of the 0th element of rank1array", True)

rank2array = np.array([[1, 2, 3],
                       [4, 5, 6]])
hold(rank2array, "Create a two-dimensional/rank 2 array", True)

hold(rank2array.shape, "Print the shape of rank2array", True)

hold([rank2array[0, 0],
      rank2array[0, 1],
      rank2array[1, 0]], "Print specific elements of rank2array", True)

zerosarray = np.zeros((2, 2))
hold(zerosarray, "Create a rank 2 array full of zeros", True)

onesarray = np.ones((1, 2))
hold(onesarray, "Create a rank 2 array full of ones", True)

constantarray = np.full((3, 2), 7)
hold(constantarray, "Create a rank 2 array full of sevens", True)

randomarray = np.random.random((2, 2))
hold(randomarray, "Create a rank 2 array full of random numbers", True)

array3x4 = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12]])
hold(array3x4.shape, "Shape of our 3x4 array", False)
hold(array3x4, "Create a rank 2 array with a shape of 3 x 4", True)

# NOTE: Pulls first two rows, then columns 1 and 2
arrayslice = array3x4[:2, 1:3]
hold(arrayslice, "Cut a slice from the array3x4 array", True)

hold(arrayslice[0, 0], "Show arrayslice[0, 0]", True)

arrayslice[0, 0] = 100
hold(arrayslice[0, 0], "Change arrayslice[0, 0] to 100", True)

longerarray =  np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9],
                         [10,  11,  12]])
hold(longerarray, "A longer array of shape (4, 3)", True)

arrayofindices = np.array([0, 2, 0, 1])
hold(arrayofindices, "Our array of indices", True)

hold([longerarray[np.arange(4), arrayofindices]], "Picking out individual points from our array of indices", True)

longerarray[np.arange(4), arrayofindices] += 10
hold(longerarray, "Adding 10 to specific points by our array of indices", True)

booleanindex = (longerarray > 5)
hold(booleanindex, "Testing each point against our boolean index", True)

hold(longerarray[booleanindex], "Just show those points that pass our test", True)

shortlist1 = np.array([[1, 2],
                       [3, 4]])
hold(shortlist1, "Short list #1", True)

shortlist2 = np.array([[5, 6],
                       [7, 8]])
hold(shortlist2, "Short list #2", True)

hold(shortlist1 + shortlist2, "Elementwise sum", True)

hold(np.add(shortlist1, shortlist2), "Elementwise sum, TIMTOWTDI", True)

hold(shortlist1 - shortlist2, "Elementwise difference", True)

hold(np.subtract(shortlist1, shortlist2), "Elementwise difference, TIMTOWTDI", True)

hold(shortlist1 * shortlist2, "Elementwise product", True)

hold(np.multiply(shortlist1, shortlist2), "Elementwise product, TIMTOWTDI", True)

hold(shortlist1 / shortlist2, "Elementwise division", True)

hold(np.divide(shortlist1, shortlist2), "Elementwise division, TIMTOWTDI", True)

hold(np.sqrt(shortlist1), "Elementwise square root", True)

shortlist3 = np.array([3, 5])
hold(shortlist3, "Short list #3", False)

shortlist4 = np.array([7, 11])
hold(shortlist4, "Short list #4", True)

hold(shortlist3.dot(shortlist4), "Product of vectors", False)
hold(np.dot(shortlist3, shortlist4), "Product of vectors, TIMTOWTDI", True)

# Rank 1 array of matrix product
hold(shortlist1, "Reminder of short list #1", False)
hold(shortlist3, "Reminder of short list #3", False)
hold(shortlist1.dot(shortlist3), "Rank 1 array of matrix/vector product", True)

# Rank 1 array of matrix product #2
hold(shortlist2, "Reminder of short list #2", False)
hold(shortlist4, "Reminder of short list #4", False)
hold(np.dot(shortlist2, shortlist4), "Rank 1 array of matrix/vector product, TIMTOWTDI", True)

# Rank 2 array of matrix product
hold(shortlist1, "Reminder of short list #1", False)
hold(shortlist2, "Reminder of short list #2", False)
hold(np.dot(shortlist1, shortlist2), "Rank 2 array of matrix/vector product", True)

# Sum columns
hold(shortlist1, "Reminder of short list #1", False)
hold(np.sum(shortlist1), "Sum of all elements", False)
hold(np.sum(shortlist1, axis=0), "Sum of all elements vertically", False)
hold(np.sum(shortlist1, axis=1), "Sump of all elements horizontally", True)

# Tons of mathematical functions
#  See https://docs.scipy.org/doc/numpy/reference/routines.math.html

hold(shortlist1, "Reminder of short list #1", False)
hold(shortlist1.T, "Transpose our array", True)

hold(shortlist3, "Reminder of short list #3", False)
hold(shortlist3.T, "Transposing a rank 1 array does nothing", True)
