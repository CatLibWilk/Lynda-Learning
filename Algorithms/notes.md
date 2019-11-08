# Chpt. 2 - Linked Lists (2.2-.3)
- List of nodes that reference the next node
- used because of efficient insertion/deletion
- used to implement stacks, queues

# Chpt. 2 - Stacks and Queues (2.4)
- stack: collection that supports push/pop operations last in/first out (last item pushed (on) in the first item popped (off))
    - used for backtracking (like in a browser), or expression processing
- queue: supports adding/removing, but on first in/ first out principle (new items added to end)
    - used for things like order processing and messaging

# Chpt. 2 - Stack/queue examples (2.6)
- python Collections module has `deque` which acts as queue (first in first out)
from Collections import deque

queue = deque
deque.append(1)
deque.append(2)
x = deque.popleft()
print(x) ==> '1'

# Chpt. 2 - hash table (2.7)
- `dictionary` in some languages
- `associative array` that maps keys to their associated values with hash function 
- typically faster than other types of table lookup structures

# Chpt. 3 - recursion (3.1)
- `recursion` when a function calls itself from inside itself
- each time the function is called the old arguments are saved ("call stack")
-  simple example:
    def countdown(x):
        if x == 0:
            print("Done!")
            return
        else:
            print(x, "...")
            countdown(x-1)


    countdown(5)

# Chpt. 4 Sorting Data
- bubble sort: first two values compared, if 1 > 2, they swap and continue, until list is in order
- nested for-loops generally indicate Big O time complexity of n2 (quadratic) 

- merge sort: uses recursion, takes set of data and breaks into parts 
    - good for large datasets big o = log n
    items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    ex.
    def mergesort(dataset):
        if len(dataset) > 1:
            mid = len(dataset) // 2
            leftarr = dataset[:mid]
            rightarr = dataset[mid:]

            # recursively break down the arrays
            mergeSort(leftarr)
            mergeSort(rightarr)

            # now perform the merging
            i=0 # index into the left array
            j=0 # index into the right array
            k=0 # index into merged array

            # while both arrays have content
            while i < len(leftarr) and j < len(rightarr):
                if leftarr[i] < rightarr[j]:
                    dataset[k] = leftarr[i]
                    i += 1
                else:
                    dataset[k] = rightarr[j]
                    j += 1
                k += 1

            # if the left array still has values, add them
            while i < len(leftarr):
                dataset[k] = leftarr[i]
                i += 1
                k += 1

            # if the right array still has values, add them
            while j < len(rightarr):
                dataset[k] = rightarr[j]
                j += 1
                k += 1
- quick sort:
    - also divides data for processing and uses recursion
    - operates on data in-place (no extra memory reqs)

# Chpt. 5 Searching for Data
- searching in an unordered list:
    -Big O linear time complexing
    -basically for i in range, if i == sth, return i

- searching in an ordered list:
    - if ordered, can perform binary search
    - get upper and lower indexes, calculate midpoint, and keep excluding values until find
    - ex
        def binarysearch(item, itemlist):
        # get the list size
        listsize = len(itemlist) - 1
        # start at the two ends of the list
        lowerIdx = 0
        upperIdx = listsize

        while lowerIdx <= upperIdx:
            # calculate the middle point
            midPt = (lowerIdx + upperIdx)// 2

            # if item is found, return the index
            if itemlist[midPt] == item:
                return midPt
            # otherwise get the next midpoint
            if item > itemlist[midPt]:
                lowerIdx = midPt + 1
            else:
                upperIdx = midPt - 1

        if lowerIdx > upperIdx:
            return None
