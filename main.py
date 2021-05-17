print("welcome to tip calculator!!")
amount=float(input("enter the full amount:"))
people=int(input("enter the no of persons:"))
tips=int(input("enter your generosity percentage 5,10,15?"))
tip=tips/100
tot_cent=amount*tip
tot_amt=amount+tot_cent
split=tot_amt/people
print(split)
