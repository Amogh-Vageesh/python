class parentcar:
    def __init__(self, color, engine):
        self.color = color
        self.engine = engine
    def show_traits(self):
        print(f"Car color : {self.color}")
        print(f"Car engine : {self.engine}")

class kid(parentcar):
    def __init__(self, name, miles, color, engine):
        self.name = name
        self.miles = miles
        super().__init__(color,engine)

    def show_traits(self):
        print(f"Name : {self.name}")
        print(f"Miles : {self.miles}")
        super().show_traits()

    def age(self,age):
        print(f"{self.name} is {age} years old")

child = kid("Bugatti", 1246, "black", "V6")

child.show_traits()
child.age(45)

print(f"Is child a subclass of parent car? {issubclass(kid, parentcar)}")