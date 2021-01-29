# Intro
- classes have `__init__` function where all the object's initial attributes are defined
    - takes `self` and any other of the classes arguments as arguments
- some attributes not defined in `init`. For those, have to use `hasattr` to check for attribute existence before trying to return or use
    - eg.
    ```
    if hasattr(self, "name"):
    ```

# "Private" attributes
- python doesnt have a way to make attributes private to only within the class, or strictly "internal"
    - common practice is underscoring the attribute eg. `self._attributename`
    - Can use double underscore ( `__attributename` ) and the attribute wont be able to easily reached outside of the class, but this can be overridden by affixing the classname with underscore before this ( `_AClass__attributename` )
        - double underscoring is used when you want to make sure that a subclass doesnt use an attribute name already used in parent class

# Class vs. Static methods and attrs
- `instance methods` receive a specific object instance as an argument and operate on data specific to that object instance
- `class properties` are shared at the class level across all instances of their class
```
"""https://realpython.com/instance-class-and-static-methods-demystified/"""
class MyClass:
    def method(self):
        return 'instance method called', self ## can modify both instance and class state

    @classmethod
    def classmethod(cls):
        return 'class method called', cls  ## CANT modify instance state, just class state

    @staticmethod
    def staticmethod():
        return 'static method called'  ## CANT modify either instance or class state, primarily for namespacing
```
- `static methods`: not many great use-cases, but one is where you dont need to access object/class properties, but where the method should belong to the class ("namespacing methods"), rather than creating a global function
    - used with `Singleton Design`: ie. where only one instance of particular variable/object is ever createds
        - eg from course: Book class will have method to track of a list of books created, 
        ```
        @staticmethod
        def getbooklist():
            if Book.__booklist == None:
                Book.__booklist = []
            return Book.__booklist
        ```
        - could just have global list variable and append to it, but this keeps it expolicitly associated with book class

## inheritence
- in children classes, use the `super().__init__( vars_to_init )` in the child's `__init__` to initialize the variables from the parent class

- `abstract base classes`: tool for enforcing set of constraints on consumers of parent classes
    - want parent-like class to build other classes with but:
        - dont want consumers of base class to be able to instantiate the base class itself
        - enforce constraint that there are certain methods in base class that children HAVE TO implement
    - need ABC module (abstract base class): `from ABC import ABC, abstractmethod`
        - parent class inherits from ABC: `def Parent( ABC ):...`
        - use `@abstractmethod` decorator to tell python that subclasses must implmement this method
            - ie. will force you to define the method in subclass (override parent's definition)

- multiple inheritence
    - python allows subclasses to inherit from more than one base class
    - if each base class defines the same attribute, problems
        - python uses  `method resolution order` when handling method class, looks first in the current class, then in the inherited classes `in the order given as arguments at subclass instantiation`
            - so if `MySubClass( B, A )`, and B and A have the same attribute, B's will be the one classed/referenced
            - python method `__mro__` will print the order: `print( MySubClass.__mro__ )`

## Interfaces
    - interface: by implemeneting an interface, a class makes "contract" to provide a certain behavior or capability
        - so have abrstract base class with a particular function (like returning JSON), and inherit it along with main base class among your subclasses, now the subclass must define it's version of the interface-baseclass ( I still dont get why it wou;dnt just be an abstract method of the baseclass, or why this is useful when the implementation of the abc.method could be completely different in every subclass, but whatever )