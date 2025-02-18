# Task1
print("\nTask1\n")
class Student:
    def __init__(self, name, surname, grade):
        self.name = name
        self.surname = surname
        self.grades = list(grade)

    def get_mark(self):
        score = int(input(f"Який бал ви хочете поставити {self.name} {self.surname}:  "))
        self.grades.append(score)
        print(f"Ви поставили йому {score}!")

    def info(self):

        print(f"name = {self.name} \nsurname = {self.surname} \ngrade = {self.grades}\n")

    def seredny_ball(self):
        avg_score = sum(self.grades) / len(self.grades)
        print(f"Середній бал: {avg_score}\n")


stud1 = Student("Oleg", "Molotok", [12, 7, 9, 6])
stud1.info()
stud1.get_mark()
stud1.info()
stud1.seredny_ball()

stud2 = Student("Nikita", "Bagum", [9, 6, 9, 8, 10])
stud2.info()
stud2.get_mark()
stud2.info()
stud2.seredny_ball()
stud3 = Student("Matviy", "Morin", [12, 11, 12, 12, 11, 12])
stud3.info()
stud3.get_mark()
stud3.info()
stud3.seredny_ball()

#Task2
print("\nTask2\n")

class Store:
    def __init__(self, name, place):
        self.name = name
        self.place = place

    def info(self):
        print(f"Name = {self.name} \nPlace = {self.place}")

class Department(Store):
    def __init__(self, name, place, list_of_stuff):
        super().__init__(name, place)
        self.list_of_stuff = list_of_stuff

    def info(self):
        print(f"Name = {self.name} \nPlace = {self.place} \nList of Stuff = {self.list_of_stuff}")

class Stand(Store):
    def __init__(self, name, place, count_of_elec_stuff):
        super().__init__(name, place)
        self.count_of_elec_stuff = count_of_elec_stuff

    def info(self):
        print(f"Name = {self.name} \nPlace = {self.place} \nCount of electric stuff = {self.count_of_elec_stuff}")

store = Store("Весела Бджілка", "вул. Миколайчука")
department = Department("Дитячі іграшки", "Магазин 'Весела Бджілка' вул. Миколайчука", ["конструктор лего", "М'які іграшки", "Настільні ігри", "..."])
department.info()
stand = Stand("Прилавок з павербанками", "вул. Миколайчука", 12)
stand.info()

#Task3
print("\nTask3\n")

task3r = "Task3.txt"
task3w = "Task3_res.txt"

with open("Task3.txt", "w") as prosto:
    prosto.write("""Як умру, то поховайте
Мене на могилі,
Серед степу широкого,
На Вкраїні милій,
Щоб лани широкополі,
І Дніпро, і кручі
Було видно, було чути,
Як реве ревучий.
Як понесе з України
У синєє море
Кров ворожу… отойді я
І лани, і гори —
Все покину і полину
До самого бога
Молитися… а до того
Я не знаю бога.
Поховайте та вставайте,
Кайдани порвіте
І вражою злою кров’ю
Волю окропіте.
І мене в сем’ї великій,
В сем’ї вольній, новій,
Не забудьте пом’янути
Незлим тихим словом.""")


def count(Task3):
    with open("Task3.txt", "r") as file:
        lines = file.readlines()
        numb_lines = len(lines)
        numb_words = sum(len(line.split()) for line in lines)

    print(f"Кількість рядків: {numb_lines}")
    print(f"Кількість слів: {numb_words}")
    return numb_lines, numb_words

def rewrite_file(numb_lines, numb_words):
    with open("Task3_res.txt", "w") as file:
        file.write(f"Кількість рядків: {numb_lines} \nКількість слів: {numb_words}")

file = "Task3.txt"
numb_lines, numb_words = count(file)
rewrite_file(numb_lines, numb_words)

# Task4
print("\nTask4\n")

balls = [6, 5, 4, 7, 8, 2, 9, 10]

for i in balls:
    if i >= 4:
        print("Ура він здав🤑")
    else:
        print("На жаль у нього не вийшло здати😭😥")


# Task5
print("\nTask5\n")

investichii = ["microsoft - 3000", "google - 2000", "apple - 5000", "tesla - 500"]
def find_investichii(company_n):
    print(f"Інвестиції у {company_n}: ")
    find = False
    for i in investichii:
        if company_n in i:
            print(i)
            find = True
    if find == False:
        print("Немає інвестицій")

company_n = input("Введіть назву компанії: ")
find_investichii(company_n)
