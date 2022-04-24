def average(grades):
    """Расчет средней оценки"""
    evaluations = []
    k = 0
    for cours, grade in grades.items():
        evaluations.append(sum(grade))
        k += len(grade)
    return sum(evaluations) / k


def aver_student(student_list):
    """Расчет средней оценки по всем студентам"""
    courses_list = {}
    for student in student_list:
        for courses, grades in student.grades.items():
            if courses in courses_list:
                courses_list[courses] += grades
            else:
                courses_list[courses] = grades
    for courses, grades in courses_list.items():
        print(f'{courses}: {sum(grades)/len(grades):.2f}')


def aver_lecturer(lecturer_list):
    """Расчет средней оценки по всем лекторам"""
    courses_list = {}
    for lecturer in lecturer_list:
        for courses, grades in lecturer.grades.items():
            if courses in courses_list:
                courses_list[courses] += grades
            else:
                courses_list[courses] = grades
    for courses, grades in courses_list.items():
        print(f'{courses}: {sum(grades) / len(grades):.2f}')


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {average(self.grades):.2f}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}\n"
        )
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Для сравнения выбраны не ученики")
            return
        return  average(self.grades) < average(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {average(self.grades):.2f}\n"
        )
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Для сравнения выбраны не лекторы")
            return
        return  average(self.grades) < average(other.grades)



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
        res = (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
        )
        return res


best_student = Student('Ruoy', 'Eman', 'man')
best_student.courses_in_progress += ['Python']

super_student = Student('Naly', 'Verc', 'woman')
super_student.courses_in_progress += ['Python', 'GIT', 'Java']

student_list = [best_student, super_student]

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'GIT', 'Java']

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 9)

cool_reviewer.rate_hw(super_student, 'Python', 10)
cool_reviewer.rate_hw(super_student, 'Python', 10)
cool_reviewer.rate_hw(super_student, 'Python', 10)
cool_reviewer.rate_hw(super_student, 'GIT', 10)
cool_reviewer.rate_hw(super_student, 'GIT', 7)
cool_reviewer.rate_hw(super_student, 'Java', 9)

best_lecturer = Lecturer("Oleg", "Bulygin")
best_lecturer.courses_attached += ['Python']

best_student.rate_hw(best_lecturer, 'Python', 10)
best_student.rate_hw(best_lecturer, 'Python', 10)
best_student.rate_hw(best_lecturer, 'Python', 10)

good_lecturer = Lecturer("Alexandr", "Bardin")
good_lecturer.courses_attached += ['Python']

best_student.rate_hw(good_lecturer, 'Python', 4)
best_student.rate_hw(good_lecturer, 'Python', 5)
best_student.rate_hw(good_lecturer, 'Python', 6)

lecturer_list = [best_lecturer, good_lecturer]

print(best_student.grades)
print(super_student.grades)
print(best_lecturer.grades)

print(cool_reviewer)
print(best_lecturer)
print(good_lecturer)
print(best_student)
print(super_student)
print(good_lecturer < best_lecturer)
print(best_student > super_student)
print()
aver_student(student_list)
print()
aver_lecturer(lecturer_list)