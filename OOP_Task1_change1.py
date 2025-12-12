class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        """Магический метод __str__ для класса Student."""
        return (f"Имя: {self.name}" + "\n" +
                f"Фамилия: {self.surname}" + "\n" +
                f"Средняя оценка за домашние задания: {self.average_grade_hw}"+ "\n" +
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}"+ "\n" +
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __eq__(self, other):
        """Магический метод __eg__ (==) для сравнения экземпляров класса Student."""
        if isinstance(other, Student):
            return self.average_grade_hw == other.average_grade_hw
        else:
            return NotImplemented

    def __lt__(self, other):
        """Магический метод __lt__ (<) для сравнения экземпляров класса Student."""
        if isinstance(other, Student):
            return self.average_grade_hw < other.average_grade_hw
        else:
            return NotImplemented

    def __gt__(self, other):
        """Магический метод __gt__ (>) для сравнения экземпляров класса Student."""
        if isinstance(other, Student):
            return self.average_grade_hw > other.average_grade_hw
        else:
            return NotImplemented

    @property
    def average_grade_hw(self):
        """Метод вычисляет среднюю оценку за домашние задания среди всех оценок Student."""
        total_grade = [] # список оценок по всем курсам
        if len(self.grades) == 0:
            return 0
        for course in self.grades:
            total_grade += self.grades[course]
        return round(sum(total_grade) / len(total_grade), 2)


    def add_new_course(self, course):
        """Метод добавляет новый курс в список текущих курсов"""
        if course not in self.courses_in_progress:
            self.courses_in_progress.append(course)
        else:
            raise TypeError("Cтудент уже изучает данный курс.")

    def add_finished_course(self, course):
        """Метод добавляет курс в список завершённых курсов и удаляет его из текущих курсов.
        Критерий: количество оценок по курсу равно 5."""
        if course in self.courses_in_progress and len(self.grades[course]) == 5:
            self.finished_courses.append(course)
            self.courses_in_progress.remove(course)
        else:
            raise TypeError("Студент не изучает данный курс или не выполнил условия завершения курса")

    def rate_lecture(self, lecturer, course, grade):
        """Метод добавляет оценку (grade) лектору (lecturer) по курсу (course)
            с занесением данных в словарь в формате {'course' (key) : grade (value)}
        """
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and (
                grade in range(11)):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return NotImplemented

class Mentor:
    """Родительский класс для преподавателей."""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс Lecturer, наследуемый от Mentor."""
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def __str__(self):
        """Магический метод __str__ для класса Lecturer."""
        return (f"Имя: {self.name}" + "\n" + f"Фамилия: {self.surname}"
                + "\n" + f"Средняя оценка за лекции: {self.average_grade_lectures}")

    def __eq__(self, other):
        """Магический метод __eg__ (==) для сравнения экземпляров класса Lecturer."""
        if isinstance(other, Lecturer):
            return self.average_grade_lectures == other.average_grade_lectures
        else:
            return NotImplemented

    def __lt__(self, other):
        """Магический метод __lt__ (<) для сравнения экземпляров класса Lecturer."""
        if isinstance(other, Lecturer):
            return self.average_grade_lectures < other.average_grade_lectures
        else:
            return NotImplemented

    def __gt__(self, other):
        """Магический метод __gt__ (>) для сравнения экземпляров класса Student."""
        if isinstance(other, Lecturer):
            return self.average_grade_lectures > other.average_grade_lectures
        else:
            return NotImplemented

    @property
    def average_grade_lectures(self):
        """Метод для определения средней оценки за лекции среди всех оценок Lecturer."""

        total_grade = []  # список оценок по всем курсам
        if len(self.grades) == 0:
            return 0
        for course in self.grades:
            total_grade += self.grades[course]
        return round(sum(total_grade) / len(total_grade), 2)

       
class Reviewer(Mentor):
    """Класс Reviewer, наследуемый от Mentor."""

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        """Магический метод __str__ для класса Lecturer."""
        return f"Имя: {self.name}" + "\n" + f"Фамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        """Метод выставления оценки (grade) за домашнее задание студенту (lecturer)
            по  курсу (course) с занесением данных в словарь
            в формате {'course' (key) : grade (value)}."""
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and (
                grade in range(11)):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return NotImplemented


def average_grade_course(grades: list, course: str):
    """Функция для подсчёта средней оценки
    (в качестве аргументов принимает список с оценками (grades)
    и название предмета (course)."""
    if grades == []:
        raise ValueError("Список с оценками пустой.")
    elif course not in grades:
        raise ValueError("Данного курса нет в списке оценок.")
    elif len(grades[course]) == 0:
        return 0
    else:
        return sum(grades[course]) / len(grades[course])

def average_grade_students(students: list, course: str):
    """Функция для подсчета средней оценки за домашние задания по всем студентам
    в рамках конкретного курса (в качестве аргументов принимает список студентов
    (students: Student) и название курса (course)."""
    total_score = 0
    for student in students:
        if isinstance(student, Student) and ((course in student.courses_in_progress) or (course in student.finished_courses)):
            total_score += average_grade_course(student.grades, course)
    return round(total_score, 2)

def average_grade_lecturers(lecturers: list, course: str):
    """Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
    (в качестве аргументов принимает список лекторов (lecturers: Lecturer) и название курса
    (course)."""
    total_score = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            total_score += average_grade_course(lecturer.grades, course)
    return round(total_score, 2)




# Создание экземпляров класса Lecturer

lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Семён', 'Семёнов')

# Создание экземпляров класса Reviewer
reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Сидор', 'Сидоров')

print('Проверка успешной реализации дочерних классов Lecturer и Reviewer')
print(isinstance(lecturer_1, Mentor)) # True
print(isinstance(reviewer_1, Mentor)) # True
print(lecturer_1.courses_attached) # []
print(reviewer_1.courses_attached) # []
print('-'*30)

# Создание экземпляров класса Student
student_1 = Student('Алёхина', 'Ольга', 'Ж')
student_2 = Student('Мелехин', 'Владимир', 'М')

# Создание списков студентов и лекторов для подсчёта средних оценок
students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]

# Присвоение студентам курсов для прохождения
student_1.add_new_course('Python')
student_1.add_new_course('Java')
student_2.add_new_course('Git')
student_2.add_new_course('C++')

# Присвоение лекторам курсов лекций
lecturer_1.courses_attached += ['Python', 'C++']
lecturer_2.courses_attached += ['Git', 'Java']

# Присвоение экспертам курсов для проверки домашних заданий
reviewer_1.courses_attached += ['Python', 'C++']
reviewer_2.courses_attached += ['Git', 'Java']



print('Попытка студента поставить оценку лектору, который не читает данный курс')
print(student_2.rate_lecture(lecturer_1, 'Git', 8))  # Ошибка

print('Попытка студента, не посещающего данный курс, поставить оценку лектору')
print(student_2.rate_lecture(lecturer_1, 'Python', 8))  # Ошибка

# Заполнение оценок первого лектора для подсчёта среднего балла
print('Попытка студента, посещающего данный курс, поставить оценку лектору, который его ведёт')
print(student_1.rate_lecture(lecturer_1, 'Python', 9))
student_1.rate_lecture(lecturer_1, 'Python', 10)



student_2.rate_lecture(lecturer_1, 'C++', 7)
student_2.rate_lecture(lecturer_1, 'C++', 8)

# Заполнение оценок второго лектора для подсчёта среднего балла
student_2.rate_lecture(lecturer_2, 'Git', 9)
student_2.rate_lecture(lecturer_2, 'Git', 2)
student_1.rate_lecture(lecturer_2, 'Java', 1)
student_1.rate_lecture(lecturer_2, 'Java', 4)
print('-'*30)
print('Попытка эксперта поставить оценку студенту, который не посещает данный курс')
print(reviewer_1.rate_hw(student_1, 'С++', 1)) # Ошибка

print('Попытка эксперта, не курирующего данный курс, поставить оценку студенту')
print(reviewer_1.rate_hw(student_1, 'Java', 1)) # Ошибка

# Заполнение оценок экспертов за домашние задания первого студента для подсчёта среднего балла
print('Попытка эксперта, курирующего данный курс, поставить оценку студенту, который его посещает')
print(reviewer_1.rate_hw(student_1, 'Python', 1))
reviewer_1.rate_hw(student_1, 'Python', 2)
reviewer_1.rate_hw(student_1, 'Python', 2)
reviewer_1.rate_hw(student_1, 'Python', 2)
reviewer_1.rate_hw(student_1, 'Python', 2)
# Перевод курса из текущих в завершённые
student_1.add_finished_course('Python')

reviewer_2.rate_hw(student_1, 'Java', 3)
reviewer_2.rate_hw(student_1, 'Java', 4)

# Заполнение оценок экспертов за домашние задания второго студента для подсчёта среднего балла
reviewer_1.rate_hw(student_2, 'C++', 5)
reviewer_1.rate_hw(student_2, 'C++', 6)
reviewer_2.rate_hw(student_2, 'Git', 7)
reviewer_2.rate_hw(student_2, 'Git', 8)
print('-'*30)

# Информация, выводимая в соответствии с заданием 3
print('Эксперт 1')
print(reviewer_1)
print('-'*30)
print('Эксперт 2')
print(reviewer_2)
print('-'*30)
print('Лектор 1')
print(lecturer_1)
print(lecturer_1.grades) # оценки студентов, поставленные лектору 1
print('-'*30)
print('Лектор 2')
print(lecturer_2)
print(lecturer_2.grades) # оценки студентов, поставленные лектору 2
print('-'*30)
print('Студент 1')
print(student_1)
print(student_1.grades) # оценки экспертов, поставленные студенту 1
print("Курс 'Python' завершён, поставлены все 5 оценок.")
print('-' * 30)
print('Студент 2')
print(student_2)
print(student_2.grades)  # оценки экспертов, поставленные студенту 2
print('-'*30)

# Использование функции подсчёта средней оценки студентов по каждому из 4-х курсов
print("Средние оценки студентов по курсу 'Python':", average_grade_students(students, 'Python'))
print("Средние оценки студентов по курсу 'Java':", average_grade_students(students, 'Java'))
print("Средние оценки студентов по курсу 'C++':", average_grade_students(students, 'C++'))
print("Средние оценки студентов по курсу 'Git':", average_grade_students(students, 'Git'))
print('-'*30)

# сравнение объектов классов Student и Lecturer на основе средних оценок (задание 3)
print(f'средняя оценка студента 1 ({student_1.average_grade_hw}) < средняя оценка студента 2 ({student_2.average_grade_hw}) ', student_1 < student_2)
print(f'средняя оценка студента 1 ({student_1.average_grade_hw}) = средняя оценка студента 2 ({student_2.average_grade_hw}) ', student_1 == student_2)
print(f'средняя оценка студента 1 ({student_1.average_grade_hw}) > средняя оценка студента 2 ({student_2.average_grade_hw}) ', student_1 > student_2)
print(f'средняя оценка лектора 1 ({lecturer_1.average_grade_lectures}) < средняя оценка лектора 2 ({lecturer_2.average_grade_lectures}) ', lecturer_1 < lecturer_2)
print(f'средняя оценка лектора 1 ({lecturer_1.average_grade_lectures}) = средняя оценка лектора 2 ({lecturer_2.average_grade_lectures}) ', lecturer_1 == lecturer_2)
print(f'средняя оценка лектора 1 ({lecturer_1.average_grade_lectures}) > средняя оценка лектора 2 ({lecturer_2.average_grade_lectures}) ', lecturer_1 > lecturer_2)
print('-'*30)

# Использование функции подсчёта средней оценки студентов по каждому из 4-х курсов
print("Средние оценки лектора по курсу 'Python':", average_grade_lecturers(lecturers, 'Python'))
print("Средние оценки лектора по курсу 'Java':", average_grade_lecturers(lecturers, 'Java'))
print("Средние оценки лектора по курсу 'C++':", average_grade_lecturers(lecturers, 'C++'))
print("Средние оценки лектора по курсу 'Git':", average_grade_lecturers(lecturers, 'Git'))


