import random


def makeList(size):
    a = [0]
    for i in range(size - 1):
        a.append(a[-1] + random.randint(1, 4))
    return a

def shuffle(a):
    for i in range(0, len(a)):
        j = random.randint(0, len(a)-1)
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

def bubbleSort (a):
    numSteps = 0
    for j in range(0, len(a)):
        for i in range(0, len(a) - 1-j):
            numSteps += 1
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
    return numSteps

def selectionSort (a):
    numSteps = 0
    for i in range(0, len(a) - 1):
        indexSmallest = i
        for j in range(i, len(a)):
            numSteps += 1
            if (a[j] < a[indexSmallest]):
                indexSmallest = j
        temp = a[i]
        a[i] = a[indexSmallest]
        a[indexSmallest] = temp

myList = makeList(10)
print(myList)
shuffle(myList)
selectionSort(myList)
print(myList)

# for n in range(10, 1000, 10):
#    myList = makeList(n)
#    shuffle((myList))
#    numSteps = bubbleSort(myList)
#    print(n, numSteps)

