hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))



if hours > 40 :
    reg = rate * hours
    opt = (hours - 40) * (rate - 40)
    print(reg,opt)
    xp = reg * opt
else:
    print(regular)
    xp = rate  * hours
     
print("Pay",xp)
