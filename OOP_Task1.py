class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    """Перегружен магический метод __str__ для класса Student в соответствии с заданием 3 

    """

    def __str__(self):
        return (f"Имя: {self.name}" + "\n" +
                f"Фамилия: {self.surname}" + "\n" +
                f"Средняя оценка за домашние задания: {self.avarage_grade_hw}"+ "\n" +
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}"+ "\n" +
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    """ Перегружен магический метод __eg__ (==) для сравнения экземпляров класса Student

    """
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.avarage_grade_hw == other.avarage_grade_hw
        else:
            return 'Ошибка'

    """ Перегружен магический метод __lt__ (<) для сравнения экземпляров класса Student

    """
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avarage_grade_hw < other.avarage_grade_hw
        else:
            return 'Ошибка'

    """ Перегружен магический метод __gt__ (>) для сравнения экземпляров класса Student

    """
    def __gt__(self, other):
        if isinstance(other, Student):
            return self.avarage_grade_hw > other.avarage_grade_hw
        else:
            return 'Ошибка'

    """ Метод для определения средней оценки за домашние задания среди всех оценок Student

    """
    @property
    def avarage_grade_hw(self):
        summ = 0
        lenn = 0
        if len(self.grades) == 0:
            return 0
        for course in self.grades.keys():
            for grade in self.grades.values():
                summ += sum(grade) / len(grade)
                lenn += 1
        return summ / lenn

    """ Метод выставления оценки (grade) лектору (lecturer) по  курсу (course) 
    с занесением данных в словарь в формате {'course' (key) : grade (value)}

    """
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

""" Класс Lecturer, наследуемый от Mentor (задание 1)

"""
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    """Перегружен магический метод __str__ для класса Lecturer в соответствии с заданием 3 

    """
    def __str__(self):
        return (f"Имя: {self.name}" + "\n" + f"Фамилия: {self.surname}"
                + "\n" + f"Средняя оценка за лекции: {self.avarage_grade_lectures}")

    """ Перегружен магический метод __eg__ (==) для сравнения экземпляров класса Lecturer

    """
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.avarage_grade_lectures == other.avarage_grade_lectures
        else:
            return 'Ошибка'

    """ Перегружен магический метод __lt__ (<) для сравнения экземпляров класса Lecturer

    """
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.avarage_grade_lectures < other.avarage_grade_lectures
        else:
            return 'Ошибка'

    """ Перегружен магический метод __gt__ (>) для сравнения экземпляров класса Student

    """
    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.avarage_grade_lectures > other.avarage_grade_lectures
        else:
            return 'Ошибка'

    """ Метод для определения средней оценки за лекции среди всех оценок Lecturer

    """
    @property
    def avarage_grade_lectures(self):
        summ = 0
        lenn = 0
        for course in self.grades.keys():
            for grade in self.grades.values():
                summ += sum(grade)/len(grade)
                lenn += 1
        return summ / lenn

""" Класс Reviewer, наследуемый от Mentor (задание 1)

"""
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    """Перегружен магический метод __str__ для класса Lecturer в соответствии с заданием 3 

    """
    def __str__(self):
        return f"Имя: {self.name}" + "\n" + f"Фамилия: {self.surname}"

    """ Метод выставления оценки (grade) за домашнее задание студенту (lecturer) 
    по  курсу (course) с занесением данных в словарь 
    в формате {'course' (key) : grade (value)}

    """
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



""" Функция для подсчета средней оценки за домашние задания по всем студентам 
в рамках конкретного курса (в качестве аргументов принимает список студентов 
(students : Student) и название курса (course : string);

"""
def avarage_grade_students(students,course):
    summ = 0

    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
           summ += sum(student.grades[course]) / len(student.grades[course])

    return summ

""" Функция для подсчета средней оценки за лекции всех лекторов в рамках курса 
(в качестве аргументов принимает список лекторов (lecturers : Lecturer) и название курса
(course : string);

"""
def avarage_grade_lecturers(lecturers,course):
    summ = 0

    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
           summ += sum(lecturer.grades[course]) / len(lecturer.grades[course])

    return summ

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
student_1.courses_in_progress += ['Python', 'Java']
student_2.courses_in_progress += ['Git', 'C++']

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
print(student_1.rate_lecture(lecturer_1, 'Python', 1))
student_1.rate_lecture(lecturer_1, 'Python', 2)
student_2.rate_lecture(lecturer_1, 'C++', 7)
student_2.rate_lecture(lecturer_1, 'C++', 8)

# Заполнение оценок второго лектора для подсчёта среднего балла
student_2.rate_lecture(lecturer_2, 'Git', 9)
student_2.rate_lecture(lecturer_2, 'Git', 10)
student_1.rate_lecture(lecturer_2, 'Java', 3)
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
print('-'*30)
print('Студент 2')
print(student_2)
print(student_2.grades) # оценки экспертов, поставленные студенту 2
print('-'*30)

# Использование функции подсчёта средней оценки студентов по каждому из 4-х курсов
print("Средние оценки студентов по курсу 'Python':", avarage_grade_students(students, 'Python'))
print("Средние оценки студентов по курсу 'Java':", avarage_grade_students(students, 'Java'))
print("Средние оценки студентов по курсу 'C++':", avarage_grade_students(students, 'C++'))
print("Средние оценки студентов по курсу 'Git':", avarage_grade_students(students, 'Git'))
print('-'*30)

# сравнение объектов классов Student и Lecturer на основе средних оценок (задание 3)
print(f'средняя оценка студента 1 ({student_1.avarage_grade_hw}) < средняя оценка студента 2 ({student_2.avarage_grade_hw}) ', student_1 < student_2)
print(f'средняя оценка студента 1 ({student_1.avarage_grade_hw}) = средняя оценка студента 2 ({student_2.avarage_grade_hw}) ', student_1 == student_2)
print(f'средняя оценка студента 1 ({student_1.avarage_grade_hw}) > средняя оценка студента 2 ({student_2.avarage_grade_hw}) ', student_1 > student_2)
print(f'средняя оценка лектора 1 ({lecturer_1.avarage_grade_lectures}) < средняя оценка лектора 2 ({lecturer_2.avarage_grade_lectures}) ', lecturer_1 < lecturer_2)
print(f'средняя оценка лектора 1 ({lecturer_1.avarage_grade_lectures}) = средняя оценка лектора 2 ({lecturer_2.avarage_grade_lectures}) ', lecturer_1 == lecturer_2)
print(f'средняя оценка лектора 1 ({lecturer_1.avarage_grade_lectures}) > средняя оценка лектора 2 ({lecturer_2.avarage_grade_lectures}) ', lecturer_1 > lecturer_2)
print('-'*30)

# Использование функции подсчёта средней оценки студентов по каждому из 4-х курсов
print("Средние оценки лектора по курсу 'Python':", avarage_grade_lecturers(lecturers, 'Python'))
print("Средние оценки лектора по курсу 'Java':", avarage_grade_lecturers(lecturers, 'Java'))
print("Средние оценки лектора по курсу 'C++':", avarage_grade_lecturers(lecturers, 'C++'))
print("Средние оценки лектора по курсу 'Git':", avarage_grade_lecturers(lecturers, 'Git'))

