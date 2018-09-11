def computepay(h,r):
    if h <= 40.0 :
        pay = h * r
    else :
        pay = (40.0 * r) + ((h - 40.0) * r * 1.5)
    return pay

try :
    h = float(raw_input("Enter Hours: "))
    r = float(raw_input("Enter rate: "))
except :
    print("You have to input numbers. Try again.")
    quit()

p = computepay(h,r)
print(p)
