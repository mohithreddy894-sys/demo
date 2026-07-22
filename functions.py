'''def even(n):
    if n%2==0:
        return True
    else:
        return False
print(even(31))


def odd(n):
    if n%2 !=0:
        return True
    else:
        return False
print(odd(45))'''



'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=int(input("enter"))
print(fact(n))'''

# sum of individual digits of a given number using recursion
'''def summ(n):
    if n==0:
        return 0
    
    return (n%10)+summ(n//10)
n=int(input("enter"))
print(summ(n))'''

#[1122,[10,20],50]=[11,22,10,20,50]
#[11,20[[40,50],25],[[45,65,[55,60]]]

'''def flatten(l):
    fl=[]
    for ele in l:
        if type(ele)==int:
            fl.append(ele)
        else:
            fl.extend(flatten(ele))
    return fl
print(flatten([11,22,[10,20],50]))
# print(flatten([11,20,[[40,50],25],[[45,65,[55,60]]]]))'''

'''l=[1,2,3,4,5]
r=map(lambda l:l*l,l)
print(list(r))'''

'''l=[10,20,30,40]
r=map(lambda l:l+10,l)
print(list(r))'''
'''n=[15,20,30,45,60,75,90,100]
r=map(
    lambda n: n**2,
    filter(lambda n:n%3==0 and n%5==0,n)


)
print(list(r))'''

'''numbers = [15, 20, 30, 45, 60, 75, 90, 100]

result = map(
    lambda x: x ** 2,
    filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers)
)

print(list(result))'''


