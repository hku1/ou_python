# # Python crash course chapter 11, oef 3 class

class Employee:
    def __init__(self, first, last, salary):
        self.first:str = first
        self.last:str = last
        self.salary:int = salary

    def give_raise(self, change=5000):
        self.salary += change
        return self.salary

# e = Employee('Harmjan', 'Kuipers', 90000)
# print(e.__dict__)
#
# e.give_raise()
# print(e.__dict__)
#
# e.give_raise(10000)
# print(e.__dict__)
