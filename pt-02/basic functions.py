import time
# funkcje <- positional arguments
def msg(username, amount, date):
    for x in range(3):
        print(f"Hello {username}\nyour bill of ${amount:.02f} is due: {date}")
msg("John", 44.11, "20.05.2025")

# return
def addNum(x, y):
    return x + y
print(f"returned value = {addNum(1, 3)}")

def createName(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
print(createName("spongebob", "squarepants"))

# funkcje <- default arguemnts == przypisanie argumentom jakis konkrentych wartosci w na stracie
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)
print(net_price(500))
print(net_price(500, 0.1))

# def counter(end, start=0):
#     for x in range(start, end + 1):
#         print(x)
#         time.sleep(1)
#     print("done")
# counter(10)

# funkcje <- keyword arguments == arguemnt z przypisanym juz typem
def print_data(message, name, age):
    print(f"{message}, {name} {age}")
print_data(name="Ziutek", message="Witaj", age="20")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
num = get_phone(country=48, area=111, last=666, first=2222)
print(num)

# arbitary <- jesli nie wiemy ile uzytkownik da argumentow
# *args <- tuple
# **kwargs <- dictionary

#*args
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1, 2, 3,5))

def show_name(*args):
    for arg in args:
        print(arg, end=" ")
show_name("Mrg","Jan","JanRapowanie","Jankowski")

#**kwargs
print()
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    
print_address(street="123 sloneczna", 
              city="rzeszuwu", 
              state="podkarpackie",
              postCode="38-111")

def shipping(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print("dane dostawy")
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    

shipping("John", "Doe", street="123 sloneczna", city="rzeszuwu", state="podkarpackie", postCode="38-111")