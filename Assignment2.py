iNum= int(input("Enter a number:"))
if iNum < 1 :
    print("Cannot perform operation")
else:
    dThisdict={i:i**2 for i in range(1,iNum+1)}
    print(dThisdict)