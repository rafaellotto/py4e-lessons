try :
    score = float(raw_input("Enter a score between 0.0 and 1.0: "))
except :
    print("Please enter a number.")

if score > 1.0 or score < 0.0 :
    print("Enter a number between 0.0 and 1.0")
    quit()

if score >= 0.9 :
    print("A")
elif score >= 0.8 :
    print("B")
elif score >= 0.7 :
    print("C")
elif score >= 0.6 :
    print("D")
else :
    print("F")
