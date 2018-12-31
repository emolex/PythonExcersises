class Parent():

    def __init__(self):
        print("******************** Initialize Parent ********************")

    def parentsMethod (self):
        print("parents Method")

    def commonMethod (self):
        print("Common method for parent and child")


class Child (Parent):

    def __init__(self):
        super().__init__()
        print("\n ******************** Initialize Child ********************")

    def commonMethod(self):
        print("Child method before super()")
        super().commonMethod()
        print("Child method after super()")


# parent = Parent( )
# parent.parentsMethod()
# parent.commonMethod()

child = Child()
# child.parentsMethod()
child.commonMethod()