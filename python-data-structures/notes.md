# Chpt 1 Abstract Data Types (ADT)
    - theoretical concept to specify what kind of data a data structure can hold and what kinds of operations are allowed on the data.
    - want to understand how to interact with it, not necessarily how implemented
    - two styles: Imperitive and Functional
        - Imperitive: data type is mutable, can be in different states at different times
            - order of operation execution is important
        - Functional: data type is immutable, separate entity of ADT for each state 
            - order of peration execution not important, no operation is changing the present state
    
    - data structure: concrete implementation of ADT
        - for every operation allowed on ADT, data structure defines one method

# Chpt 2 Stack Data Structure
    - holds collection of items in order added, can only add and remove from top (last in first out) 
        *"top" of stack is the right side (what I would call the end of the list but whatever)*
    - Python list is built-in datatype that represents a stack
    - `limited access data structure`: can only access data from one place in structure
    - stack is recursive: is either empty, or consists of a top item and the rest of the stack

    - Building a Stack Class (starting 02_03)
        - include push (adds item to end of list), pop, peek, size, is_empty methods
        - push: runs 0(1) `constant time` 
            - `push` method will just be `self.items.append(item)`
            - `peek' will be `return self.items[-1]`
        - should pythonically check that stacks aren't empty when doing push and peek with:
            if stack.items:
                return ...
            else 
                return None
        - is_empty method: return stack.items == [] (return True if stack is equal to empty list, else false)

# Chpt 3 Queue Data Structure
    - hold collection of items in order in which added (FIFO - first in first out)
        - right side ("front") of a python list is "front" of list, items taken from front in constant time, added to "back" of list (ie. at 0 index) in linear time, because each addition changes the indexes for each item 
        - queue is `limited access` because can only access data from one place
        - useful when need to access data in order that it became available
        - also `recursive`: queue is either empty or consists of first item and rest of queue
    
    - queue class will have enqueue, dequeue, peek, size, and is_empty methods

    - enqueue
        - rather than `append` as with stack, will use `insert`
            ie. def enqueue(self, item):
                    self.items.insert(0, item)
    - dequeue
        - uses .pop() (removes last item in list)
            - requires check to see if list is populated before trying to pop (or will error)
    
    - peek: return self.items[-1] (will of course need check make sure list is not empty)

# Chpt 4 Deque ("DECK")
    - `double-ended queue`
    - abstract datatype resembling both a stack and queue
    - items can be added and removed both from front and back
    - will also use python list to implement deque
    - uses FIFO and/or LIFO (last in first out) models at same time
    - can choose which end of list is 'front' because will use linear runtime regardless of which end accessing data
    - used in common interview question: check if word is a palindrome
    - methods
        - because remove from front and end, method names need to distinguish between add/remove from front and from back
        - add/remove_front, add/remove_rear, peek_front/rear, size
        - add_front/rear
            - front `self.items.insert(0, item)`
            - rear `self.items.append(item)`
        -remove_front/rear
            - front `self.items.pop(0)` //pop item from 0th index
            - rear `self.items.pop()`
            - !needs check for non-empty list
                - if self.items:
                    return self.items.pop()
                  return None

# Chpt Next Steps/External Resources
    - Problem Solving with Algorithms and Data Structures using Python
        - `https://runestone.academy/runestone/books/published/pythonds/index.html`