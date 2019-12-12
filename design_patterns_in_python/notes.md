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

- Pattern context
    - participants: classes in design pattern
    - quality attributes: non-functional reqs
    - forces: factors or trade-offs, manifested in quality attributes
    - consequences

## Chpt. 2 - Creational Patterns
- 1. Factory
    - encapsulates object creation
    - useful when uncertain about type of objects needed, or when decisions about what classes to use occur at runtime
    - ex. 
        class Shape(object):
            # Create based on class name:
            def factory(type):
                #return eval(type + "()")
                if type == "Circle": return Circle()
                if type == "Square": return Square()
                assert 0, "Bad shape creation: " + type
            factory = staticmethod(factory)

        class Circle(Shape):
            def draw(self): print("Circle.draw")
            def erase(self): print("Circle.erase")

        class Square(Shape):
            def draw(self): print("Square.draw")
            def erase(self): print("Square.erase")

        # Generate shape name strings:
        def shapeNameGen(n):
            types = Shape.__subclasses__()
            for i in range(n):
                yield random.choice(types).__name__

        shapes = \
        [ Shape.factory(i) for i in shapeNameGen(7)]
            - so calling Shape.factory(i) where i is the shape name yielded from the generator will produce an list of created circle and square objects

        for shape in shapes:
            shape.draw()
            shape.erase()

- 2. Abstract factories (exfiles 2_04)
    - user expects family of related objects at runtime, but doesn't know which family until runtime

- 3. Singleton: object-oriented way of providing global variables (exfiles 2_06)
    - allow only one object to be instantiated from a class
    - can act as cache of info to be shared by various objects in system, so dont have to retrieve from source every time

- 4. Builder (exfiles 2_08)
    - design pattern solution to 'telescoping constructor' anti-pattern
        - ie. problem occuring when trying to build complex object with excessive number of constructors
    - partitions building a complex object into 4 different roles
        - director  
        - abstract builder (Provides interfaces)
        - concrete builder (implements interfaces)
        - product - represents actual object being built

- 5. Prototype(exfiles 2_10)
    - clones objects according to prototypical instance
        - useful for creating many identical objects individually
    - make class Prototype with 4 methods
        - one instantiating an object dict, two to add/remove objects to dict with name argument as key
        - another to clone using imported module `copy` as `copy.deepcopy(self._objects.get(name))` [`where self._objects is dict created in __init__ method at top`]

- 6. Decorators (3_02)
    - adds additional features to existing function
    - uses `@` symbol

- 7. Proxy (3_04)
    - useful when dealing with resource-intensive object
    - goal is to postpone object creation until absolutely necessary
    - need for placehold that creates object if necessary
    - clients interact with proxy object until resource-intensive object becomes available

- 8 Adapter(3_06)
    - adapts interface of class into one the client is expecting
        - usage ex.: incompatible interface between client and server
    - can have individualized method names in classes that do the same thing, running through adapter could generalize them
        - e.g. speak_english(), speak_korean() ==> speak()

- 9 Composite(3_08)
    - maintains tree data structure to represent part/whole relationships
    - ex. = creating menu and submenu items
    - three parts: 
        - Component: abstract class
        - Child: concrete class inheriting from component
        - Composite: concrete class inheriting from component
    