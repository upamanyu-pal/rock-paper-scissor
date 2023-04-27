import random
rps = ['r','p','s']

c_chooses = random.choice(rps)
u_chooses = input("Enter your choice: ")

dif = rps.index(c_chooses) - rps.index(u_chooses)

print(f"Computer chose {c_chooses}.")
print('\n')

if dif==0:                            # tie
    print("Whoops! It's a tie.")

elif abs(dif)==1:                     # difference of one
    if dif>0:
        print("Computer wins")
    else:
        print("You win")

elif abs(dif)==2:                     # difference of two
    if dif>0:
        print("You win")
    else:
        print("Computer wins")