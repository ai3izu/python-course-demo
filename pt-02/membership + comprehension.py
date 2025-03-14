#membership operations in , not in
#uzycie string, list, tuple, set, dictionary
word = "APPLE"
letter =(input("guess a letter in a word "))
if letter in word:
    print(f"there is a {letter}")
else : print(f"there is not a {letter}")

students = {"Spongebob" , "Saul", "Mike"}
student = input("enter the name of student ")
if student not in students:
    print("there is no such a student")
else : print("bingo!")

grades = {
    "Walter":3,
    "Spongebob":5,
    "Hector":4
}
studentGrade = input("enter a name of a student ")
if studentGrade in grades:
    print(f"{studentGrade} grade is  {grades[studentGrade]}")
else : print("student was not found")


#list comprehension <- [expression for value in iterable if condition]

#przyklad na zwyklej petli
# doubles = []
# for x in range (1,11):
#     doubles.append(x * 2)
# print(doubles)

#przyklad list comprehension
doubles = [x * 2 for x in range(1,11)]
triples = [y * 3 for y in range (1,16)]
print(doubles)
print(triples)

fruits = ["apple", "orange", "banana"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

nums = [1,-2,-3,-5,-6]
positive_nums = [num for num in nums if num >= 0]
negative_nums = [num for num in nums if num < 0]
print(positive_nums)
print(negative_nums)

grades = [85,40,77,23,65,11]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)
