y = 9
x = 25

for i in range(0 , 30):
    x = x-1
    if x == (-1):
        y -= 1
        x = 59
    continue

print("Hours "+str(y) +"  ||  "+ "Minutes "+str(x))

def percents(b,c):
    if (b == 0) or (b <= 7):
        c = y
        b = 0
        return "Hours "+str(c),"Minutes in percent "+str(b)
    elif (b > 7) and (b <= 22):
        c = y
        b = 25;
        return "Hours "+str(c),"Minutes in percent "+str(b)
    elif (b > 22) and (b <= 37):
        c = y
        b = 50;
        return "Hours "+str(c),"Minutes in percent "+str(b)
    elif (b > 37) and (b <= 52):
        c = y
        b = 75;
        return "Hours "+str(c),"Minutes in percent "+str(b)
    elif (b > 53) and (b <= 59):
        c = y + 1;
        b = 0;
        return "Hours "+str(c),"Minutes in percent "+str(b)

print(percents(x,y))