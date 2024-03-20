'''i = int(input("Enter any no"))
if i%2!=0:
    print("Weird")
    
elif i%2 ==0 and 2<=i<=5:
    print("Not Weird")
    
elif i%2==0 and 6<=i<=20:
    print("Weird")
    
if i>20 and i%2==0:
    print("Not Weird")'''
    
def sum1(num):
    if not num:
        return 0
    else:
        return num[0]+ sum1(num[1:])
print(sum1([2,7,17,15]))
