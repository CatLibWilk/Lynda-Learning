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

## composition
- can build complex objects from simpler ones with composition rather than inheritance, whereby there is a "has" relationship (book has author) rather than the "is" relationship inherent in inheritence (Book is publication). 
    - so eg. have an Author and Book class:
    ```
    class Book:
        def __init__(self, title, price, author=None):
            self.title = title
            self.price = price

            # Use references to other objects, like author
            self.author = author

    class Author:
        def __init__(self, fname, lname):
            self.fname = fname
            self.lname = lname

    leo_tolstoy = Author('Leo', 'Tolstoy')
    war_and_peace = Book('War and Peace', '30', leo_tolstoy)
    ```

## Magic Methods
- python associates a set of methods with every class
    - can be overridden
- string methods
    - __str__(returns string about object) and __repr__ (object representation)
- comparison methods
    - cant just go `instantiation1 == instantiation2` if to check if two objects are the same (ie. have the same values/variables). Python doesn't check variable by variable on objects
        - have to define the __eg__ function in class (eg):
        ```
        def __eq__(self, value):
            if not isinstance(value, Book):
                raise ValueError("Can't compare book to non-book type")

            return (self.title == value.title and
                    self.author == value.author and
                    self.price == value.price)
        ```
        - can define similar methods for all the comparison types (greater than, less than, etc. )
        - once less than is defined, can use the `.sort()` method on a list of objects for example

- attribute access
    - can alter how class attributes are accessed and handled with __getattribute__
        - eg. when price called, return price with discount applied automatically
        ```
        class Book:
        def __init__(self, title, author, price):
            super().__init__()
            self.title = title
            self.author = author
            self.price = price
            self._discount = 0.1

        # Called when an attribute is retrieved. Be aware that you can't
        # directly access the attr name otherwise a recursive loop is created
        def __getattribute__(self, name):
            if (name == "price"):
                p = super().__getattribute__("price")
                d = super().__getattribute__("_discount")
                return p - (p * d)
            return super().__getattribute__(name)
        ```
        - have to directly access attribute name with `super().__getattribute__` because otherwise will loop recursively
    - can do the same with controlling how attributes are set ( __setattr__ )
        - eg. 
        ```
        def __setattr__(self, name, value):
            if (name == "price"):
                if type(value) is not float:
                    raise ValueError("The 'price' attribute must be a float")
            return super().__setattr__(name, value)
        ```
        
## Data Classes
- starting with python 3.7, can automate the creation and managing of classes that mostly exist just to hold data with `data classes`
    - import: `from dataclasses import dataclass`
    - use `@dataclass` decorator and then just declare attributes and their data types
    ```
    @dataclass
    class Book:
        title: str
        author: str
        pages: int
        price: float
    ```
    - decorator rewrites code in compile to effectively reinsert the __init__ function and assign to `self` params
- dataclasses also automatically implement the `__repr__` and `__eq__` methods 
- `dataclass` decorator lets you customize additional properties that rely on other properties after the object has been initialized
    - ie. if you have attributes that rely on other attributes (eg. `price` = `self.base_price` - `self.discount`), cant define as normal because the decorator eliminates the usual `__init__` function. 
    - `dataclass` has the `__post_init__` method
    - eg.
    ```
    @dataclass
    class Book:
        title: str
        author: str
        pages: int
        price: float

        # the __post_init__ function lets us customize additional properties
        # after the object has been initialized via built-in __init__
        def __post_init__(self):
            self.description = f"{self.title} by {self.author}, {self.pages} pages"
    ```
    
    ## Immutability
    - can make objects immutable with the @dataclass decorator
        - set `frozen = true` in the decorator arguments
        ```
        @dataclass( frozen = true )
        class ImmutableClass():
            value1: 'value1 '
            ...
        ```