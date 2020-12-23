class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __get_average_rate(self):
        rate_accum = 0
        rates_count = 0
        for key, rate_array in self.grades.items():
            for rate in rate_array:
                rate_accum += rate
                rates_count += 1

        if rates_count > 0:
            return rate_accum / rates_count

        return 0

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print("Ошибка!")

    def __str__(self):
        returned_value = f'Имя: {self.name}\n'
        returned_value += f'Фамилия:  {self.surname}\n'

        average_rate = self.__get_average_rate()

        if average_rate != 0:
            returned_value += f'Средняя оценка за домашние задания: {average_rate}\n'
        else:
            returned_value += 'У студента нет оценок\n'

        if len(self.courses_in_progress) > 0:
            returned_value += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        else:
            returned_value += 'У студента отсутствуют курсы в процессе изучения\n'

        if len(self.finished_courses) > 0:
            returned_value += f'Завершенные курсы: {", ".join(self.finished_courses)}'
        else:
            returned_value += 'У студента отсутствуют завершенные курсы'

        return returned_value

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.__get_average_rate() < other.__get_average_rate()
        else:
            raise TypeError()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        super().__init__(name, surname)

    def __get_average_rate(self):
        rate_accum = 0
        rates_count = 0
        for key, rate_array in self.grades.items():
            for rate in rate_array:
                rate_accum += rate
                rates_count += 1

        if rates_count > 0:
            return rate_accum / rates_count

        return 0

    def __str__(self):
        returned_value = f'Имя: {self.name}\n'
        returned_value += f'Фамилия:  {self.surname}\n'

        average_rate = self.__get_average_rate()

        if average_rate != 0:
            returned_value += f'Средняя оценка за лекции: {average_rate}'
        else:
            returned_value += 'Лектору не ставили оценок'
        return returned_value

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.__get_average_rate() < other.__get_average_rate()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        returned_value = f'Имя: {self.name}\n'
        returned_value += f'Фамилия:  {self.surname}'
        return returned_value


def get_avg_students_rate(student_list, course):
    rate_accum = 0
    rate_count = 0
    for student in student_list:
        if course in student.grades:
            for grade in student.grades[course]:
                rate_accum += grade
                rate_count += 1

    if(rate_count>0):
        return rate_accum/rate_count

    return 0


def get_avg_lecturers_rate(lecturers_list, course):
    rate_accum = 0
    rate_count = 0
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            for grade in lecturer.grades[course]:
                rate_accum += grade
                rate_count += 1

    if (rate_count > 0):
        return rate_accum / rate_count

    return 0


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress.append('Python')
best_student.courses_in_progress.append('Git')

other_student = Student('John', 'Wick', 'male')
other_student.courses_in_progress.append('Python')

python_lecturer = Lecturer('John', 'Karmak')
python_lecturer.courses_attached += ['Python']

worst_lecturer = Lecturer('Jason', 'Born')
worst_lecturer.courses_attached += ['Python']

python_reviewer = Reviewer('Jack', 'Rassel')
python_reviewer.courses_attached += ['Python']

python_reviewer.rate_hw(best_student, 'Python', 10)
python_reviewer.rate_hw(best_student, 'Python', 10)

python_reviewer.rate_hw(other_student, 'Python', 10)
python_reviewer.rate_hw(other_student, 'Python', 7)

best_student.rate_lecturer(python_lecturer, "Python", 10)
best_student.rate_lecturer(worst_lecturer, "Python", 3)
best_student.rate_lecturer(worst_lecturer, "Python", 5)

students_list = [best_student, other_student]
lecturers_list = [python_lecturer, worst_lecturer]

print(get_avg_students_rate(students_list, 'Python'))
print(get_avg_lecturers_rate(lecturers_list, 'Python'))

# print(best_student > other_student)
# print(python_lecturer > worst_lecturer)
# print()
#
# print(python_lecturer)
# print(python_reviewer)
# print(other_student)
