#Random GAme
import random
limit=1
while True:
    if limit<=3:
        X=random.randrange(1,6)
        Y=int(input("ENter the limit 1-5: "))
        if Y==X:
            print(f"Congratulations, You Win","Attempts =",limit)
            break
        else:
            print(f"Sorry, You Lose, the number was:{X}","And You Have", (3-limit),"attempts left")
        limit+=1
        
print("Thankyou")
   
print("Finished")