number = input("enter a positive number.")
digits = len(number)
summ = 0
if not number.isdigit() :
    print(number, "is invalid entry. enter numberic value!")
    number = input("please enter a numeric value")
elif int(number) >= 0 :
    for i in range(digits) :
        summ = summ + int(number[i]) ** digits
    if summ == int(number) :
        print(number, "is an Armstrong Number.")
        
    else :
        print(number, "is not an Armstrong Number.")
    