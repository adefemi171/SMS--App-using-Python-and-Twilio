def money(amount):
    if (amount == '1ksh'):
        min = '1 mins'
    elif (amount == '2ksh'):
        min = '2 mins'
    elif (amount == '5ksh'):
        min = '5 mins'
    elif (amount == '20ksh'):
        min = '20 mins'
    else:
        print("No amount entered")
    return min



a = input("How much did you pay? ")
c = (str(a) + str('ksh')) 
mins = money(c)
print(mins)