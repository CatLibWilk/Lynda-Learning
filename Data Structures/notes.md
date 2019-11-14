# Chpt. 1 Intro. to Data Structures
- primitive datatypes: ints, doubles, floats, long/shorts, chars, booleans
 - have fixed size that doesn't depend on information stored (int will always be 32-bits no matter the value)

 # Chpt. 4 Stacks and Queues
 - Python has DEQUEK ("DECK", double-ended queue) class
 - Deque can be implemented in python using the module “collections“. Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.

 # Chpt. 5 Hash-based structures
 - hash function: inputing raw data to produce hash value. "hash value" simplified reference generated from raw values.
    - hash function non-reversible, can't get original values from processing hash
    - ex. hash function generates hash of a password, login puts your input through h-function to see if it matches hash, but doesn't de-hash the hash value stored.

- python has `GetHashCode` function

# Chpt. 6 Sets/trees (test membership)
- sets take an object and generate a hash of it, rather than a hash table with an object and hash as key
  - dont use sets for data retrieval
- in python3:
  - variable = set(['one', 'tow', 'three'])

- trees
  - structure is a root node with parent/child nodes below
- binary search tree
  - constraint: max two child nodes/parent, left child must be less than parent, right child more than parent
  - for javascript or python, need to use third-party library
