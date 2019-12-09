## Chpt. 1
- 3 Types of Design Patterns 
    - creational: used to create objects in systematic way
        - main benefit is flexibility
        - frequently relies on polymorphism
    - structural: establish useful relationships between software components in certain configs
        - takes advantage of inheritance
    - behavioral: best practices of object interaction
        - relies on methods and their signatures 
    - interfaces are used across all these types of patterns

- inheritance
    - establishes parent/child relationship between two classes
        - child keeps methods/attributes of the parent
        - can add new methods/attributes
        - can override parent attrib/methods

- polymorphism: define methods in the child class with the same name as defined in their parent class
    - relies on inheritance
    - allows child classes to be instantiated and treated as same type as parent
    - enables parent class to be manifested into any of its child classes
    - If a child class object is used to call an overridden method then the child class version of the method is called. On the other hand, if parent class object is used to call an overridden method, then the parent class version of the method is called.