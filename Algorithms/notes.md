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