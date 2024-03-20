'''
# scope of variable and act like object
def fun():
    print("MANISHA IS MY LOVE AND LIFE")
fun()
test = fun
test()
fun.name = 'ABHIJEET'
print(fun.name)
'''

'''
# Polymorphisum function
def fun(am):
    for i in am:
        print(i*2)
fun([10,20,30,40])
fun('MA')
'''
''' # global and local variable 
x = 10
def main():
    sum = x + y
    print(sum)
y = 20
main()
'''
''' # local and global variable
a = 18
def main():
    a = 9
    print('local a:',a)
    m = 16
    print('local m:',m)
    sum = a + m
    print(sum)
main()
print('global a',a)'''

''' # dynamic function
a = 18
def fun():
    a = 9
    def g():
        print('outer the g def value of a: ',a)
    g()
fun()'''
''' # dynamic function
a = 18
def fun():
    global a
    a = 9
    print('global value a ',a)
fun()'''

'''# local and global function checking
am = 16
def fun():
    am = 9
    print(' inside a fun value of a ',am)
    def g():
        nonlocal am
        print('inside g, before modifying value of am = ',am)
        am = 18
        print('inside g after modifying value of am= ',am)
    g()
    print('inside fun after calling g value of am= ',am)
fun()
print('after calling fun value of am= ',am)
'''

'''# displying the list value and empty the list
am =[1,2,3,4,5,6]
def fibo(am):
    if not am:
        return
    else:
        print(am[0])
        print(am[1:])
        fibo(am[1: ])
fibo(am)'''

'''# calculate sum of all the element in a list using recursion
def sum1(am):
    if not am:
        return 0
    else:
        return am[0]+ sum1(am[1:])
st = sum1([10,20,30,40])
print(st)'''

'''
def st(am):
    if not am:
        return ' '
    else:
        return st(am[1: ])+ am[0]
print(st("I love my love manisha"))
'''
'''
def fun(a,m):
    print('first:',a)
    print('second:',m)
fun(10,20)
fun(m=10,a=20)
'''

'''factorial using recuirsion
def factorial(am):
    #assert am>=0
    if am ==0 or am ==1:
        return 1
    else:
        return am * factorial(am-1)
def main():
    am = int(input('Enter the number: '))
    rest = factorial(am)
    print(rest)
main()
'''
''' specify values argument that are not passed '''
def fun ( a , m):
    print('first:',a)
    print('second:',m)
st = (9,16)
fun(*st)
st = {'m': 9,'a':16}
fun(**st)
