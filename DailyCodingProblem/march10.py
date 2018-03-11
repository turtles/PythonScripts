# Given an array of integers, find the first missing positive integer
# in linear time and constant space. In other words, find the lowest
# positive integer that does not exist in the array. The array can
# contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2.
# The input [1, 2, 0] should give 3.

def firstMissingPositiveInt(arr):
    positives = []
    for i in range(0,len(arr)):
        if arr[0]>0:
            positives.append(False)
    print(positives)

    for i in range(0,len(arr)):
        if arr[i]>0:
            positives[arr[i]-1] = True

    print(positives)

    for i in range(0,len(positives)):
        if (positives[i]==False):
            return i+1

    return len(positives)+1


print(firstMissingPositiveInt([1,3,4,-1]))