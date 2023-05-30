height = input("write the input of heights ").split()
for n in range (0,len(height)):
    height[n]=int(height[n])
print(height)

total_height=0
for i in height:
    total_height=total_height+i
print(total_height)

number=0
for j in height:
    number+=1
print(number) 

average_height= round(total_height/number)
print(average_height)

