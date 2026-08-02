"""#ДЗУрок1 :
1. Создать класс Person с атрибутами fullname, age, is_married
2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем, где ключ это название урока, а значение - оценка.
4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience. 
6. Добавить в класс Teacher атрибут уровня класса base_salary
7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3-х лет.
8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и список возвращается функцией как результат.
10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам."""



class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'ИМЯ: {self.fullname}\t ВОЗРАСТ: {self.age}\t СЕМЕЙНОЕ ПОЛОЖЕНИЕ: {self.is_married}')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks: dict):
        super().__init__(fullname, age, is_married)

        self.marks = marks


    def GPA_calculator(self, marks):
        self.discipline_count = 0
        self.points_count = 0

        for i in marks:
            self.discipline_count += 1
            self.points_count += marks[i]
        self.GPA = self.points_count / self. discipline_count
        return round(self.GPA, 1)            


    def introduce_myself(self):
        print(f'ИМЯ: {self.fullname}\t ВОЗРАСТ: {self.age}\t СЕМЕЙНОЕ ПОЛОЖЕНИЕ: {self.is_married}\nОЦЕНКИ ПО КАЖДОМУ ПРЕДМЕТУ:\n{self.marks}\nGPA УЧЕНИКА: {self.GPA_calculator(self.marks)}')


class Teacher(Person):
    base_salary = 100000
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)

        self.experience = experience

    def salary_calculator(self):
        if self.experience > 3:
            self.salary = self.base_salary * (1+(((self.experience-3) * 5) / 100))
            return round(self.salary)
        else:
            return self.base_salary

        
english_teacher = Teacher('Zhypar', 30, 'Замужем', 5)
english_teacher.introduce_myself()
print(english_teacher.salary_calculator())


def create_students(fullname, age, is_married, marks, fullname2, age2, is_married2, marks2, fullname3, age3, is_married3, marks3 ):
    student1 = Student(fullname, age, is_married, marks)
    student2 = Student(fullname2, age2, is_married2, marks2)
    student3 = Student(fullname3, age3, is_married3, marks3)

    stud_list = [student1, student2, student3]
    return stud_list

students = (create_students('qwer', 20, 'Холост', {
    'math': 5,
    'english': 3,
    'physic' : 4
}, 'asdf', 21, 'Холост',{
    'math': 5,
    'english': 5,
    'physic' : 5
}, 'zxcv', 19, 'Холост', {
    'math': 3,
    'english': 5,
    'physic' : 5
}))

for i in students:
    i.introduce_myself()