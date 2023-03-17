from functools import partial
print("Enter the numbers u want to add to list, press'q' if u want to quit")
lst=[]
while True :
    try :
        lst.extend(int(i) for i in iter(partial(input,'Enter number : '), 'q'))
        break
    except ValueError :
        print("ERROR : we only allow numbers, try again please")
print(lst)  
print("The Largest Number is = " ,max(lst))
print("The Smallest Number is = " ,min(lst))