l_Alist = [5,2,1,6,8,9]
l_Blist = [34,5,6,5,6]
if len(l_Alist)<1 and len(l_Blist)<1:
    print("Cannot perform operation")
else:
    i_SumofList =sum([i**2 for i in l_Alist]) + sum([i**3 for i in l_Blist])
    print(i_SumofList)
