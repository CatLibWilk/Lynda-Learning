# Chpt. 1 OO Fundamentals

# Inheritance
- Have one class with attributes common to other classes, the other classes will inherit from the common class, and have attributes unique to them defined in own class (superclass vs. subclass)
# Polymorphism
- dynamic polymorphism: use same interface for methods on different types of objects
    - inheritance, abstract classes, and interfaces are different implementations of d-polymorphism
- static/compile-time polymorphism
    -  utilizes `method overloading`: implementing multiple methods in same class with same name, but different sets of input params

- OO analysis, design, and programming
    - analysis and design occur before code writing (what you need to do and how you'll do it)
    - typical 5-step approach: gather reqs, describe the app, ID main objects, describe the interactions, create class diagram

- Unified Modeling Language (UML)
    - standardized notation for diagrams to visualize OO systems

# Chpt. 2 Defining Requirements
- First set of reqs should be the `musts` and `shoulds`, functional and non-functional requirements, not necessarily all the features that would be nice to have
    - just those required for a minimum viable product
- FURPS requirements
    - Functionality, Useability, Reliability, Performance and Supportability

# Chpt. 3 Use Cases/User Stories
- Use Case has 3 components
    - title: what is the goal?
    - primary actor: who desires it? (can be user, or another system working on system)
    - success scenario: how is it accomplished?
    - can also describe as a series of steps toward successful conclusions
    - additional details: extensions(steps for alternate flows, e.g. if something goes wrong) and preconditions

- identifying actors
    - people AND external systems
    - actors interacting with it to meet desired outcome, but also others that need to interact with (maintenance and etc.)
- identifying scenarios
    - emphasis user-focused goals based on intent
- diagramming use cases
    - diagram includes several use cases and actors, with lines drawn showing all use-relationships between the two

# Chpt. 4 Domain Modeling
- after analysis and creation of use-cases, develop conceptual model which identifies the most important objects in the application and how the are related.
    -  pick out nouns from use cases to determine `potential` objects

- identify object responsibilities
    - select verb statements from use cases
    - objects should be responsible for self
        - ex. player steers car, but shouldn't have method in user class to directly change state in car, rather should ask car to change its directional state
    - avoid global master objects
        - responsibilities should be distributed among system objects and not stored in one master `god-object`
- CRC (Class, Responsibility, Collaborators) organization
    - can organize thinking by creating CRC cards giving class, its reponsibilities, and the other objects it interacts with

# Class Diagrams
- class entities in the diagram give class name, its attributes, and its behaviors
    - attributes: [attributeName]: [datatype] e.g. healthLevel: integer
    - behaviors: the methods = [methodName](params): [return_data_type] e.g. getHealth(): Integer, raiseHealth(Integer)
    - +/- symbols before attributes and behaviors in the diagram indicate their public/private nature (encapsulation )

- Instantiating Classes
    build constructor method within class (with same name as class) to create objects at instantiation with values in place for their attributes. 
            example.
            class Spaceship: 
                name = "" 
            
                # default constructor 
                def __init__(self): 
                    self.name = "Defaulticus"
            
                # a method for printing data members 
                def print_Spaceship(self): 
                    print(self.name) 
        
        
        # creating object of the class 
        obj = Spaceshib() 
        
        # calling the instance method using the object obj 
        obj.print_Spaceship()

- Overloading
    - creating multiple constructor methods
        - class can have multiple methods with same name, but with different params
            - e.g. one with no args, one that takes an arg
    - no overloading in Python

- static variables/methods
    - variables/methods shared across all objects in a class
    - in python, these are variables declared within a class but outside of a method
    - so if have class Spaceship, and instances spaceship1, spaceship2, accessing a static variable for all = Spaceship.variable vs. spaceship1.name spaceship2.name or similar
    - in Python, have class and static methods, with decorators @staticmethod @classmethod
        - both are bound to class not instantiated object of class
        - class methods can access class state, static cannot
    
    - Inheritence
        - python: class subClass(superClass) (class being inherited from in parens)
        - overriding (depends on language): where something in subclass overrides that in inherited
        - calling super vs. subclass methods: e.g. python :super().methodName()
    
    - abstract and concrete classes
        - abstract classes never get instantiated, they exist only to be inherited from
            - e.g. Spaceship class used to build different types of spaceship
            - abstract classes cant be implemented because they have at least one abstract method (declared with method signature but not actually implemented)
                - e.g. superclass has setShield and move functions, all subclasses will use the same setShield, so inherits and no need to declare in subclass definition, but may move differently so will have to define own move methods
    
    - Interfaces
        - method of abstraction
        - list of methods for class to implement (doesnt contain any actual behavior)
        - interfaces represent a capability, abstract classes represent a type 
        - classes can inherit from multiple interfaces
    
    - Aggregation
        - `has a` relationship ('fleet has a spaceship', where 'a' implies 'many')
        - destroying the aggregation object doesn't destroy the child objects

    - Composition
        - like aggregation, but destroying the composition destroys the children

    ## Chpt. 7
        - Python doesnt exactly support interfaces, but does by way of abstract classes
    
    - SOLID developmnet principles
        - Single responsibility principle: class should only have one responsibility (anti 'god-object')
        - open/closed principle: 
        - liskov substitution
        - interface segregation
        - dependency inversion

    - DRY principle
        - Don't Repeat Yourself
    
    - Design Patterns
        - re-usable form of a solution to common design problems
        - see book: `Design Patterns: Elements of Reusable Object-Oriented Software`