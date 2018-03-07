# Given an array of numbers, return whether any two sums to K.
# For example, given [10, 15, 3, 7] and K of 17, return true since 10 + 7 is 17.

def hasTwoElementsWhichSumToK(array, K):
    for i in range(len(array)):
        for j in range(len(array)):
            if i==j:
                continue
            elif (array[i]+array[j]) == K:
                return True

    return False


array = [10, 15, 3, 7]
K = 17
print(hasTwoElementsWhichSumToK(array,K))
