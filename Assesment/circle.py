class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

NewCircle = Circle(int(input("Enter Radius")))
print(NewCircle.area())
