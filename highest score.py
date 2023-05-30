scores= input("enter your scores").split()
for n in range(0,len(scores)):
    scores[n]=int(scores[n])
print(scores)

highest=0
for s_scores in scores:
    if s_scores>highest:
        highest=s_scores
print(f"The highest score in the class is :{highest}")






    
