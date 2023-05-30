name1= input("enter your name")
name2= input("enter lovers name")
joined= name1+name2
low=joined.lower()
t= low.count("t")
r= low.count("r")
u= low.count("u")
e= low.count("e")
l= low.count("l")
o= low.count("o")
v= low.count("v")
 
true= t + r + u + e
love= l + o + v + e

lovers= int(str(true) + str(love))

if lovers<10:
    print("you go togetyher like cola and mentos")
elif lovers<60:
    print("You guys are alright")
else:
    print("You guys are LOVERSS")
