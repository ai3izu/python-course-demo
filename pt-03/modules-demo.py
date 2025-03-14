#module = to takie libki
#print(help("modules"))

#zaimportowanie modulu -> import nazwa_modulu  / mozna tez nadac wlasna nazwe przez as
import math as mata
print(mata.pi)

#import pojedynczej rzeczy z modulu
from time import gmtime
print(gmtime())

#mozna tez tworzyc wlasne i importowac (patrz plik example_module.py)
import example_module
print(example_module.hello)

test = "I've created my own module"