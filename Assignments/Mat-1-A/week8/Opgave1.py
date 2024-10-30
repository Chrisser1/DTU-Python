class Person:
    def __init__(self, name: str, cpr_number: int):
        self.__name: str = name
        self.__cpr_number: int = cpr_number
    def get_name(self):
        return(self.__name)

    def get_cpr_number(self):
        return(self.__cpr_number)

    def show(self):
        print("Name:", self.get_name(), "\nCPR number:", self.get_cpr_number())


    def __str__(self):
        return(f"Name: {self.get_name()} \nCPR number: {self.get_cpr_number()}")

    def set_name(self, name):self.__name = name


class Teacher(Person):
    number_instances: int = 0

    def __init__(self, name: str, cpr_number: int, staff_id: int, list_of_courses: list[int]):
        super().__init__(name, cpr_number)
        self.__staff_id: int = staff_id
        self.__list_of_courses: list[int] = list_of_courses
        Teacher.number_instances += 1

    def __str__(self):
        courses: str = "\nList of courses: " + ", ".join(str(i) for i in self.__list_of_courses)
        return super().__str__() + f"\nStaff id: {self.__staff_id}" + courses

    def __del__(self):
        Teacher.number_instances -= 1
        print(f"The teacher has been deleted. There is now {Teacher.number_instances} teachers")

if __name__ == '__main__':
    teacher1 = Teacher(name="Ebbe", cpr_number="3102301", staff_id=1, list_of_courses=[11234,2314])

    print(teacher1)

    del teacher1
