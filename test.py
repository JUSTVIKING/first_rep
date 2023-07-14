
from colorama import init
from colorama import Fore, Back, Style

init()

print( Back.GREEN )
print( Fore.BLACK )
what = input( "What to do? (+, -): " )

print( Back.CYAN )

a = float( input("Typ first number: ") )
b = float( input("Typ second number: ") )

print( Back.YELLOW )

if what == "+":
	c = a + b

	print("Total: " + str(c))
elif what == "-":
	c = a - b
	print("Total: " + str(c))
else:
	print("ERROR")

input()