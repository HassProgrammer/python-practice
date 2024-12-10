class Person:
    name = "anonymous"
    # def changeName(obj, name) :
    #self._class_.name = "Khan"
    
    @classmethod
    def changeName (cls, name) :
        cls.name = name
p1 = Person ( )
p1. changeName ("Ahshanul Alam")
print (p1.name)
print (Person.name)