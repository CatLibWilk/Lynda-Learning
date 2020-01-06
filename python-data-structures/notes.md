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
    - Python list is built-in datatype that represents a stack
    - `limited access data structure`: can only access data from one place in structure
    - stack is recursive: is either empty, or consists of a top item and the rest of the stack