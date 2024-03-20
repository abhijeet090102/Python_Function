'''def function (name,*args):
    print(name)
    print(args)

function(1,2,3,4,5)'''
'''
def My_func(c,v,*args,**kwargs):
    print(kwargs)
My_func(2,3,4,5,6,a=9,m=16)
'''
'''
def power(x,y):
    if y == 0:
        return 1
    else:
        return x * power(x,y-1)
print(power(2,3))
'''
'''
a = (lambda x:x*(x+1))
(6)
print(a)
'''
nu = [1,2,3,48,90]
re = list(filter(lambda x: x%2==0,nu))
print(re)
