print("john")

name = "john"
name
name[2]
name[3]
type(name)
name[0:2]

dir(str)

type(name)
type(len)
len(name)
len("vahitkesin")
len("miuul")


"miuul".upper()
"MİUUL".lower()

type(upper)


hi = "Hello AI Era"

hi.replace("l","p")


"Hello AI Era".split()

"foo".capitalize()
dir("foo")


notes = [1,2,3,4]
type(notes)

notes = ["a","b","c","d"]

not_nam = [1,2,3,4,5,"a","b","v","c",False,True,[1,2,3,4,45,6]]
type(not_nam)
not_nam[11][3]

not_nam[11][3] = 11
not_nam

dir(notes)
len(notes)
len(not_nam)
notes.append(5)
len(notes)
notes

notes.insert(2,99)
notes
notes.pop(2)
notes.pop((4))
notes.append((5))
notes.pop(5),(4)
notes.pop(4)
notes
notes.append(5)
notes
notes.insert(4,e)
notes
notes.insert(2,55)
notes
notes.pop(3)
notes.append(23)
notes

# key - value

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary["REG"]
dictionary["CART"]

dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE",20],
              "CART": ["SSE",30]}
dictionary["REG"][0]

"REG" in dictionary
"LOG" in dictionary
"RMSE" in dictionary


dictionary["REG"] = ["YSA",10]
dictionary["REG"]

dictionary.keys()
dictionary.values()
dictionary.items()





set1 = set([1,3,5])
set2 = set([1,2,3])



set1.difference(set2)
set2.difference(set1)
set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

set1.intersection(set2)
set2.intersection(set1)

set1 & set2

set1 - set2

set1.union(set2)


set3 = set([7,8,9])
set4 = set([5,6,7,8,9,10])

set3.difference(set4)
set4.difference(set3)

set3.symmetric_difference(set4)
set3.intersection(set4)
set3.union(set4)

set3.isdisjoint(set4)
set4.isdisjoint(set3)

set3.issubset(set4)
set4.issubset(set3)


####   DİFFERENCE METODU İKİ KÜMENİN FARKINI ALIR

### SİMETRİK DİFFERENCE

### UNİON İKİ KÜMENİN BİRLEŞİMİ

## İNTERSECTİON İKİ KÜMENİN KESİŞİ KODLARI EZBERLEMEYE GEREK YOK. ZATEN SIK KULLANDIKÇA AKILDA KALACAKTIR.

total = 2 + 5


print("a")

print("a", "b", sep="??")

help(print)



  ###   FONKSIYON   TANIMALAMA ####
 ############################




def calculate(x):
    """

    :param x:
    :return:
    """
      print(x*2)


 calculate(5)




 # iki argümanlı / parametreli bir fonksiyon tanımlayalım.

 def summer(arg1, arg2):
     """
     sum of two numbers

    Args:
        arg1: int , float
        arg2: int , float

         Returns:
                int , float

     """
     print(arg1 + arg2)

summer(7, 8)
summer(1,3)


def say_hi(string):
    print("merhaba")
    print("hi")
    print("Hello")

say_hi("miuul")
say_hi("selamcık")

def say_hi(int):
    say_hi("oo")
say_hi("123")
say_hi(123)
say_hi(1.2)
say_hi("selam1,2")


def multiplication(a, b):
    c = a * b
    print(c)

    multiplication(5,9)



list_store = []
def add_element(e, f):
    d = e * f
    list_store.append(d)
    print(list_store)

add_element(1, 8)
add_element(2, 5)
add_element(180, 15)


def divide(n, m=2):
    print(n / m)

divide(1)
divide(19)



### warm , moisture, charge

(56 + 15) / 80
(42 + 13) / 90
(33 + 11) / 55




def calculate(warm, moisture, charge):
    warm = warm*2
    moisture = moisture*2
    charge = charge*2
    output = (warm + moisture)/charge

    return warm, moisture,  charge, output




type(calculate(58,60,120))

warm, moisture,  charge, output = calculate(58,60,120)



list_store = [1,2]

def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(4, 3)
add_element(4, 9)




def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(13)
number_check(14)
number_check(10)


def number_control(number):
    if number > 10:
        print("bigger than 10")
    elif  number < 10:
        print("less than 10")
    else:
        print("equal to 10")

number_control(20)
number_check(20)
number_control(9)
number_control(10)



students = ["erdi", "ali", "yeko", "dodo","emre"]

students[0]
students[3]


for student in students:
    print(student.upper())

salaries = [1000,2000,3000,4000,5000,6000]

    for salary in salaries:
        print(int(salary*20/100+salary))

def new_salary(salary, rate):
    return int(salary*rate/100 + salary)

new_salary(1500, 10)
new_salary(2000, 20)


for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 20))
    elif salary >= 6000:
        print(new_salary(salary,5))

    else:
        print(new_salary(salary, 40))






students = ["John", "Mark", "Venessa", "Mariam"]
for student in students:
    print(student)

#for index, student in enumerate(students):
 #   print(index,student)

#A = []
#B = []

#for index, student in enumerate(students):
    #if index % 2 ==0:
    #    A.append(student)
   # else:
  #      B.append(student)


students = ["John", "Mark", "Venessa", "Mariam"]

def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
        print(groups)
        return groups

divide_students(students)


divide_students(students)


def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
        print(new_string)

alternating_with_enumerate("hi my name is john ı am learning python")





#def new_salary(x):
 #   return x *20 / 100 + x

#null_list = []

#for salary in salaries:
 #   if salary > 3000:
      #  null_list.append(new_salary(salary))
#    else:
     #   null_list.append(new_salary(salary * 2))



#[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

#salaries = [1000, 2000, 3000, 4000, 5000]

#[salaries * 2 if salary < 3000 else salary * 0 for salary in salaries ]




student = ["John", "Mark", "Vanessa", "Mariam"]

student_no = ["John", "Vanessa"]

[student.lower() if student in student_no else student.upper() for student in students]


[student.upper() if student not in student_no else student.lower() for student in students]



dictionary = {"a":1,
              "b":2,
              "c":3,
              "d":4}

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v for (k, v) in dictionary.items()}

{k.upper(): v ** 3 for (k, v) in dictionary.items()}



numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

{n: n ** 2 for n in numbers if n % 2 == 0}


okul_list =[ "total", "spending", "alcohol","not distracted","no_previous","ins_premium","ins_losses"]

for okul in okul_list:
    print(okul.upper())

A = []
for okul in okul_list:
    A.append(okul.upper())

okul_list = A


okul_list =[ "total", "spending", "alcohol","not distracted","no_previous","ins_premium","ins_losses"]

okul_list = [okul.upper() for okul in okul_list]

# list comprehensions ile yazıldı Kısa yol.


# Amaç key'i string , Value'su aşağıdaki gibi bir liste olan sözlük oluşturmak
########

#output :

dictionary = {"total": ["mean", "min","max","var"],
 "spending": ["mean", "min","max","var"],
 "alcohol": ["mean", "min","max","var"],
 "not_distracted": ["mean", "min","max","var"],
 "no_previous": ["mean", "min","max","var"],
 "ins_premium": ["mean", "min","max","var"],
 "ins_losses": ["mean", "min","max","var"]}

dictionary.keys()
dictionary.values()
dictionary.items()


numbers = range(1,10)
{n: n ** 2 for n in numbers if n % 2 != 0}

import numpy as np


