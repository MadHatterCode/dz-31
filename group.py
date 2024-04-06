class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_remove = list(filter(lambda x: x.last_name == last_name, self.group))
        if student_to_remove:
            self.group.difference_update(student_to_remove)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = "".join([f"{student.first_name} {student.last_name} " for student in self.group])
        return f'Number:{self.number}\n {all_students}'

    def __eq__(self, other):
        if isinstance(other, Group):
            return self.__str__() == other.__str__()