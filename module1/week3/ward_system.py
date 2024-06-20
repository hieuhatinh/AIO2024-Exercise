class Person:
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f'Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}')


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f'Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}')


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f'Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}')


class Ward:
    def __init__(self, ward_name):
        self.__ward_name = ward_name
        self.__persons = []

    def add_person(self, person):
        self.__persons.append(person)

    def count_doctor(self):
        number_doctors = 0
        for person in self.__persons:
            if isinstance(person, Doctor):
                number_doctors += 1
        return number_doctors

    def sort_age(self):
        self.__persons.sort(key=lambda person: person._yob, reverse=True)

    def compute_average(self):
        sum_yob_teachers = 0
        number_teachers = 0
        for person in self.__persons:
            if isinstance(person, Teacher):
                number_teachers += 1
                sum_yob_teachers += person._yob
        return sum_yob_teachers / number_teachers

    def describe(self):
        print(f'Ward Name: ', self.__ward_name)
        for person in self.__persons:
            person.describe()


# 2(a)
student1 = Student(name='studentA', yob=2010, grade='7')
student1.describe()

teacher1 = Teacher(name='teacherA', yob=1969, subject='Math')
teacher1.describe()

doctor1 = Doctor(name='doctorA', yob=1945, specialist='Endocrinologists')
doctor1.describe()


# 2(b)
print('-----------------')
teacher2 = Teacher(name='teacherB', yob=1995, subject='History')
doctor2 = Doctor(name='doctorB', yob=1975, specialist='Cardiologists')
ward1 = Ward(ward_name='Ward1')
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# 2(c)
print('-----------------')
print(f'Number of doctors: {ward1.count_doctor()}')

# 2(d)
print('-----------------')
print('After sorting Age of Ward1 people')
ward1.sort_age()
ward1.describe()

# 2(e)
print('-----------------')
print(f'Average year of birth (teachers): {ward1.compute_average()}')
