class Employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary
        self.__bonus=1000

    def get_bouns(self):
        return self.__bonus

emp = Employee("Nikhilesh",30000)
print(emp.name)
# emp._salary=5000
print(emp._salary)

print(emp._Employee__bonus)
emp._Employee__bonus=10000
print(emp._Employee__bonus)