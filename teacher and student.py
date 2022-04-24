def average(grades):
    "Расчет средней оценки"
    evaluations = []
    k = 0
    for cours, grade in grades.items():
        evaluations.append(sum(grade))
        k += len(grade)
    return sum(evaluations) / k


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
            f"Курсы в процессе изучения: {','.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {','.join(self.finished_courses)}\n"
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
super_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 9)

cool_reviewer.rate_hw(super_student, 'Python', 10)
cool_reviewer.rate_hw(super_student, 'Python', 10)
cool_reviewer.rate_hw(super_student, 'Python', 10)

cool_lecturer = Lecturer("Oleg", "Bulygin")
cool_lecturer.courses_attached += ['Python']

best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 10)

bad_lecturer = Lecturer("Alexandr", "Bardin")
bad_lecturer.courses_attached += ['Python']

best_student.rate_hw(bad_lecturer, 'Python', 4)
best_student.rate_hw(bad_lecturer, 'Python', 5)
best_student.rate_hw(bad_lecturer, 'Python', 6)

print(best_student.grades)
print(cool_lecturer.grades)

print(cool_reviewer)
print(cool_lecturer)
print(bad_lecturer)
print(best_student)
print(super_student)
print(bad_lecturer < cool_lecturer)
print(best_student > super_student)