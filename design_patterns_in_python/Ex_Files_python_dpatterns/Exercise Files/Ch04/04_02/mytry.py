class Subject(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Person(Subject):

    def __init__(self, name="", age=""):
        Subject.__init__(self)
        self._age = age
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age
        self.notify()

class InterestedParty:
    def __init__(self, name=""):
        self._name = name
    def update(self, subject):
        print(self._name + " Sending a card to " + subject._name + " because they turned " + str(subject._age) + " yesterday!")


andy = Person("andy", "29")
danny = Person("danny", "30")


mom = InterestedParty("mom")
dad = InterestedParty("dad")
glenner = InterestedParty("glenner")
andy.attach(mom)
andy.attach(dad)

danny.attach(glenner)

print("andy is " + andy.age)
print("danny is " + danny.age)

andy.age = 30
danny.age = 31