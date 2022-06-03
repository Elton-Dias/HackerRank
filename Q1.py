# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with  places after the decimal.

def plusMinus(arr):
    arrLength = len(arr)
    positiveNumberCount = 0
    negativeNumberCount = 0
    zeroCount = 0

    for i in range(arrLength):
        if (arr[i] > 0):
            positiveNumberCount += 1
        elif (arr[i] < 0):
            negativeNumberCount += 1
        elif (arr[i] == 0):
            zeroCount += 1

    print("{0: .6f}".format((positiveNumberCount / arrLength)), end="\n")
    print("{0: .6f}".format((negativeNumberCount / arrLength)), end="\n")
    print("{0: .6f}".format((zeroCount / arrLength)), end="\n")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)