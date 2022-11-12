a = int(input("enter a number : "))

if a >1 :
    for x in range(2,a):
        if a%x == 0:
            print("Not prime")
            break
        else :
            print('Prime')
            break
else:
    print("Not prime")