import random
import math
import time
import string

class Single:
    def __init__(self):
        self.Word = ""
        self.int1 = 0
        self.int2 = 0
        self.total = 0

    def __str__(self):
        return(str(self.Word) + " " + str(self.int1) + " " + str(self.int2))
    
def randomArray():
    start_time = time.time()
    #allowed parameters
    asciiString = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    maxInt = 2^32 - 1
    maxDouble = 2^64 - 1
    #initialization
    #number of records
    randomMain = 1300000
    listMain = []
    index = 0
    randomChar = ""

    #build Records
    for x in range(0, randomMain):
        total = 0
        word = ""
        listMain.append(Single())
        #Length of string
        randomLength = random.randint(10, 40)
        #join a randomLength of characters (randomAscii)
        #find total sum of characters
        for x in range(randomLength):
            randomChar = random.choice(asciiString)
            total = total + ord(randomChar)
            word += randomChar
            
        #Save information
        listMain[index].Word = "".join(word)
        listMain[index].int1 = random.randint(0, maxInt)
        listMain[index].int2 = random.uniform(0, maxDouble)
        listMain[index].total = total + listMain[index].int1 + listMain[index].int2
        #increment index
        index += 1
    
    print ("Done generating numbers")
    print("--- %s seconds ---" % (time.time() - start_time))
    return listMain

#Sort the total of the record - ascii values of string + int1 + int2
def quickSortTotal(myList, start, end):
    if start < end:
        # partition the list
        pivot = partitionTotal(myList, start, end)
        # sort both halves
        quickSortTotal(myList, start, pivot-1)
        quickSortTotal(myList, pivot+1, end)
    return myList

#Used in quickSortTotal
def partitionTotal(myList, start, end):
    #pick pivot to temporarily sort data
    pivot = myList[start].total
    #first number is already sorted with itself
    left = start+1
    right = end
    done = False
    #find two numbers to swap
    while not done:
        #left side of pivot
        #if the number[left] < pivot then it stays, else it is swapped to the right
        while left <= right and myList[left].total <= pivot:
            left = left + 1
        #if the number[right] > pivot then it stays, else it is swapped to the left    
        while myList[right].total >= pivot and right >=left:
            right = right -1
        #exit when all the numbers have been swapped to correct side of the pivot
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

def binarySearch(myList, start, middle, end, search):
    #cut the list in half until at the highest number
    middle = math.floor(middle)

    #find the highest number
    middleTot = myList[middle].total

    #recursively cut the list in half while moving to the end
    if (math.floor((middle + end)/ 2) == middle):
        #when the highest value is found, print it
        print (str(myList[end].Word), search)
    elif (middleTot < search):
        binarySearch(myList, middle, (middle + end) / 2, end, search)
    
def main():
    start_time = time.time()
    #initialization
    myList = []
    myList = randomArray()
    length = len(myList) - 1
    
    #sort the list
    myList = quickSortTotal(myList, 0, length)
    index = 0
    
    #print lowest 100 values
    for x in range(0, 100):
        print (str(index + 1),myList[index].Word,str(myList[index].int1),str(myList[index].int2), str(myList[index].total))
        index += 1
    print("---------------------------------")

    #binary search for highest value (last record)
    binarySearch(myList, 0, length/2, length, myList[length].total)

    print("--- %s seconds ---" % (time.time() - start_time))
    
    
#Call function
main()
