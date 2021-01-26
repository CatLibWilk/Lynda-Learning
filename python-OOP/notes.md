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