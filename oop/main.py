class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __rating(self):
        summ = int([sum(sum(el) for el in self.grades.values())][0])
        lens = int([sum(len(el) for el in self.grades.values())][0])
        return round(summ / lens, 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Лицо не является студентом'
        return self.__rating() < other.__rating()

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.__rating()} \n\
Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {",".join(self.finished_courses)}'
        return res
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __rating(self):
        summ = int([sum(sum(el) for el in self.grades.values())][0])
        lens = int([sum(len(el) for el in self.grades.values())][0])
        return round(summ / lens, 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Лицо не является лектором'
        return self.__rating() < other.__rating()

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.__rating()}'
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

first_student = Student('Максим', 'Кац', 'мужской')
first_student.courses_in_progress += ['Python']

second_student = Student('Катя', 'Шуль', 'женский')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['PythonWEb']
second_student.finished_courses += ['Web']

first_lecturer = Lecturer ('Петр', 'Первый')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer ('Александр', 'Второй')
second_lecturer.courses_attached += ['Python']

first_reviewer = Reviewer ('Настасья', 'Филипповна')

second_reviewer = Reviewer ('Мария', 'Вознесенская')
second_reviewer.courses_attached += ['Python']

second_student.rate_lec(first_lecturer, 'Python', 9)
second_student.rate_lec(first_lecturer, 'Python', 8)
second_student.rate_lec(first_lecturer, 'Python', 5)
second_student.rate_lec(first_lecturer, 'Python', 7)

first_student.rate_lec(second_lecturer, 'Python', 8)
first_student.rate_lec(second_lecturer, 'Python', 9)
first_student.rate_lec(second_lecturer, 'Python', 10)
first_student.rate_lec(second_lecturer, 'Python', 9)

second_reviewer.rate_hw(second_student, 'Python', 7)
second_reviewer.rate_hw(second_student, 'Python', 3)
second_reviewer.rate_hw(second_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'Python', 6)

second_reviewer.rate_hw(first_student, 'Python', 9)
second_reviewer.rate_hw(first_student, 'Python', 7)
second_reviewer.rate_hw(first_student, 'Python', 8)
second_reviewer.rate_hw(first_student, 'Python', 9)

list_st = [second_student, first_student]
list_lec = [first_lecturer, second_lecturer]

def all_rating_hw(list_students, course):
    rat = 0
    for student in list_students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            res = sum(student.grades[course]) / len(student.grades[course])
            rat += res
        else:
            return 'Ошибка'
    return f'Cредняя оценка за домашние задания по всем студентам\
 в рамках курса {course} равна {round(rat / len(list_students), 1)}'

def all_rating_lec(list_lecturer, course):
    rat = 0
    for lecturer in list_lecturer:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            res = sum(lecturer.grades[course]) / len(lecturer.grades[course])
            rat += res
        else:
            return 'Ошибка'
    return f'Cредняя оценка за лекции всех лекторов\
 в рамках курса {course} равна {round(rat / len(list_lecturer), 1)}'


print(second_student)
print(first_lecturer)
print(second_reviewer)
print(first_student > second_student)
print(second_student > first_student)
print(first_lecturer > second_lecturer)
print(second_lecturer > first_lecturer)

print(all_rating_hw(list_st, 'Python'))
print(all_rating_lec(list_lec, 'Python'))
