## Funciones de Cadena en Python 
print(len("Hola Mundo"))## Len() Calcula la longitud de los caracteres //  Calculate length of the characters
## Convert to string in a list
a=("the world is in preventive isolation")
listb = a.split()
print(listb)
## lower() Convert to string in a lowercase
text = "PePe iS mY Mentor"
print(text.lower())
## upper() convert to string in a capitals
print(text.upper())
## replace() replace a string for another
print(text.replace('Mentor','Teacher'))

## Numeric Functios 
## range() Create a numeric range 
x = range(6)
print (list(x))
## str() convert the int to a string 
print(str(100))
##int() convert value to a integer
##float() convert value to a float
##max() select max value of a group
x=[1,3,4,2]
print(max(x))
##min() select min value of a group
print(min(x))
##sum() sum for two values or more values
print(sum(x))

##Other Functions
##list() Create a list from a Value
x=range(4)
print(list(x))
##round() round to value 
print(round(15.58))
#datetime and date
from datetime import date
from datetime import datetime
today = date.today()
print(today)
hoy=datetime.now()
print(hoy)

## Random 
import random
a=random.randint(10,100)
print(a)
b=random.randrange(0,100,5)
print(b)
c=random.random()
print(c)
friends=['Luis','miguel','Patricia','Carlos']
winner=random.choice(friends)
print(winner)
##shufle() Order by ramdom
carts=[1,2,3,4,5,6,7,8,9]
random.shuffle(carts)
print(carts)



## Function Math 
## trunc() delete float for a value 
import math
a=123.56
b=math.trunc(a)
print(b)

##fabs() Calculate absolute value for a float, removing a sign
a=-200.45
b=math.fabs(a)
print(b)

##math.factorial() El factorial se expresa como n!. ejemplo: 0! ==
a=6
b=math.factorial(a)
print(a, b)

##fmod() return mod for a divide
c=math.fmod(16,5)
print(c)

##sqrt() eturns the square root of any number
a=3
c=math.sqrt(a)
print(c)

##sin(), cos() y tan(). Uses values at radians i can use convert grads to radians 


angle=60
radians=math.radians(angle)
print(radians)
sen=math.sin(radians)
print("seno: ",sen)
cos=math.cos(radians)
print("coseno: ",cos)
tan=math.tan(radians)
print("Tangente: ",tan)