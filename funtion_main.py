'''def main():
    a = 10;m = 20
    print(a+m)
__name__
'''
'''def main():
    a = 10;m=20
    print(a+m)
if __name__=='__main__':
    main()'''
'''def triangle():
    for i in range(0,9):
        for k in range(0,i+1):
            print('a',end=' ')
        print('\n')            
def main():
    triangle()'''
def revtria():
    row = int(input("Enter no of rows "))
    am = 2*row-2
    for i in range(0,row):
        ''' for print spaces '''
        for j in range(0,am):
            print(end=' ')
        am = am-2
        for  j in range(0,i+1):
            ''' for printing no or anything'''
            print(j,end=' ')

        print('')

def main():
    revtria()
if __name__=='__main__':
    main()
    
