import datetime

date = datetime.datetime.now()

def resp(name_number):
    splitted = name_number.split()

    name = splitted[7]
    for each in range(8, 10):
        if (splitted[each][0].isdigit()):
            mobile = splitted[each]
            break;
        else:
            name = name + " " + (splitted[each])
    val = (name + " " + mobile)
    return val


def date_time(dat_tim):
    splitted = dat_tim.split()

    __date = splitted[11]
    for each in range(12, 20):
        if (splitted[each][0].isdigit()):
            __date = __date + " " + (splitted[each])
            #mobile = splitted[each]
            break;
        else:
            __date = __date + " " + (splitted[each])
    
    return __date



message = "NB40MDZ5Q0 Confirmed. You have received Ksh530.00 from MONICA MUGA 0716103968 on " + str(date.strftime("%Y-%m-%d" + " at " + "%H:%M")) + " , New M-PESA balance is Ksh533.00. To reverse forward message to 456."
message_output = resp(message)
time_output = date_time(message)
print (message_output)
print(time_output)