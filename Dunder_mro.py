"""
    Exercice to find the path where a instance is created
"""

import sys
import inspect

class person:

    def __init__(self, name, edge, gender, birth):
        self.Name = name
        self.Edge = edge
        self.Gender = gender
        self.Birth = birth
        print("\n\n --INFORMATION--\n ")
        print(f"Input   -> {self.__dict__}\n")
        print(f"__class__.__mro__ INSIDE    -> {self.__class__.__mro__}")


class Employee(person):

    def __init__(self, name, edge, gender, birth, job, salary):
        super().__init__(name, edge, gender, birth)
        self.Job = job
        self.Salary = salary



if __name__ == '__main__':
    x = Employee(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])

    print(f"\nInspect getfile     -> {inspect.getfile(x.__class__)}\n")
    print(f"__class__.__mro__   -> {x.__class__.__mro__}\n")
    print(f"Inspect getmodule   -> {inspect.getmodule(x)}\n")



