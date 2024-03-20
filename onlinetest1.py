def main(n):
    if n%2 == 0 :    
        if (n>=2 and n <= 5 )or n>20:
            print('Not Weird')
        elif n>=6 and n<=20:
            print('Wierd')
    elif n%2 == 1:
        print('Weird')
n = int(input('Enter no => '))
main(n)
'''if __name__ ='__main__':
    if n % 2 == 1:
        print('Weird')
    else:
        if n >= 2 and n <= 5:
            print("Not Weird")
        # Check if the number is even and in the inclusive range of 6 to 20
        elif n >= 6 and n <= 20:
            print("Weird")
        # Check if the number is even and greater than 20
        else:
            print("Not Weird")'''
