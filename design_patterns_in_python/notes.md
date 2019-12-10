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

- 2. Abstract factories
    - user expects family of related objects at runtime, but doesn't know which family until runtime

- 3. Singleton: object-oriented way of providing global variables 
    - allow only one object to be instantiated from a class
    - can act as cache of info to be shared by various objects in system, so dont have to retrieve from source every time