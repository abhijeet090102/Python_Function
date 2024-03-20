'''def display(l):
    if not l:
        return
    else:
        print(l[0])
        print(l[1:])
        display(l[1:])
display([1,2,5,6,8])'''

'''def sum(l):
    if not l:
        return 0
    else:
        return l[0] + sum(l[1:])

am = sum([10,20,30,40])
print(am)'''

'''def sum(l):
    if not l:
        return ''
    else:
        return sum(l[1:])+l[0]

print(sum('MCA1st'))
'''
def sum(num):
    am = num[0]+ sum(num[1:])
    if am==9:
        return am
    else:
        return num[0]+ sum(num[1:])
print(sum([2,7,17,15]) )
