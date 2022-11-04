class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = []
        self.course = []

    def rate_lections(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached or course in self.finished_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum = 0
        len = 0
        for key in lecturer.grades.keys():
            for val in list(lecturer.grades[key]):
                sum = sum + val
                len += 1
        lecturer.average = round(sum / len, 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average < other.average

    def __str__(self):
        return f'\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average} \nКурсы в процессе обучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'\nИмя: {self.name} \nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_attached = []
        self.grades = {}
        self.average = []

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average < other.average

    def __str__(self):
        return f'\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.finished_courses = []

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress or course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum = 0
        len = 0
        for key in student.grades.keys():
            for val in list(student.grades[key]):
                sum = sum + val
                len += 1
        student.average = round(sum / len, 1)

    def __str__(self):
        return f'\nИмя: {self.name} \nФамилия: {self.surname}'


first_student = Student('Ruoy', 'Eman', 'male')
first_student.courses_in_progress += ['Python']
first_student.finished_courses += ['Введение в программирование']

second_student = Student('Violet', 'Evergarden', 'female')
second_student.courses_in_progress += ['GIT']
second_student.finished_courses += ['Введение в программирование']

first_lecturer = Lecturer('Alex', 'Polikarpov')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Marco', 'Polo')
second_lecturer.courses_attached += ['GIT']

first_reviewer = Reviewer('Some', 'Buddy')
first_reviewer.courses_attached += ['Python']

second_reviewer = Reviewer('Leman', 'Russ')
second_reviewer.courses_attached += ['GIT']

first_reviewer.rate_hw(first_student, 'Python', 7)
# first_reviewer.rate_hw(first_student, 'JAVA', 9)

first_student.rate_lections(first_lecturer, 'Python', 1)
# first_student.rate_lections(first_lecturer, 'JAVA', 5)

# second_reviewer.rate_hw(second_student, 'C++', 3)
second_reviewer.rate_hw(second_student, 'GIT', 7)

# second_student.rate_lections(second_lecturer, 'C++', 4)
second_student.rate_lections(second_lecturer, 'GIT', 7)

student_list = [first_student, second_student]

lecturer_list = [first_lecturer, second_lecturer]

comparison1 =[]
stud1 = first_student.average
lect1 = first_lecturer.average
delt1 = max(stud1, lect1) - min(stud1, lect1)
if lect1 > stud1:
    comparison1 = f'Средняя оценка лекторов отличается на {delt1}'
elif stud1 > lect1:
    comparison1 = f'Средняя оценка студентов отличается на {delt1}'
else:
    comparison1 = 'Оценки равны'

comparison2 =[]
stud2 = second_student.average
lect2 = second_lecturer.average
delt2 = max(stud2, lect2) - min(stud2, lect2)
if lect2 > stud2:
    comparison2 = f'Средняя оценка лекторов отличается на {delt2}'
elif stud2 > lect2:
    comparison2 = f'Средняя оценка студентов отличается на {delt2}'
else:
    comparison2 = 'Оценки равны'

print(f'Перечень студентов:\n\n{first_student}\n\n{second_student}')
print()

print(f'Перечень лекторов:\n\n{first_lecturer}\n\n{second_lecturer}')
print()

print(f'Результат сравнения студентов: '
      f'{first_student.name} {first_student.surname} < {second_student.name} {second_student.surname} = {first_student > second_student}')
print()

print(f'Результат сравнения лекторов: '
      f'{first_lecturer.name} {first_lecturer.surname} < {second_lecturer.name} {second_lecturer.surname} = {first_lecturer > second_lecturer}')
print()

student_list = [first_student, second_student]

lecturer_list = [first_lecturer, second_lecturer]


def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.average
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()

print(f"Средняя оценка для всех студентов по курсу {'GIT'}: {student_rating(student_list, 'GIT')}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'GIT'}: {lecturer_rating(lecturer_list, 'GIT')}")
print()

# print(f"Средняя оценка для всех студентов по курсу {'C++'}: {student_rating(student_list, 'C++')}")
# print()
#
# print(f"Средняя оценка для всех лекторов по курсу {'C++'}: {lecturer_rating(lecturer_list, 'C++')}")
# print()
#
# print(f"Средняя оценка для всех студентов по курсу {'JAVA'}: {student_rating(student_list, 'JAVA')}")
# print()
#
# print(f"Средняя оценка для всех лекторов по курсу {'JAVA'}: {lecturer_rating(lecturer_list, 'JAVA')}")
# print()

print(f'\n\n{first_student} \n{first_lecturer} \n{first_reviewer} \n{second_student} \n{second_lecturer} \n{second_reviewer} \n{comparison1} \n{comparison2}')
