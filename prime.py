#waptp in given range prime numbers 
'''def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
           
        else:
            return True
    else:
        return False
def primenumber(ll,ul):
    for i in range(ll,ul+1):
        if isprime(i):
            print(i)
primenumber(2,100)'''

#print a numbers in given range is perfect or not using functions
'''def perfect(n):
    total=0
    for i in range(1,n):
        if n%i==0:
            total+=i
    return total==n
def isperfect(ll,ul):
    for i in range(ll,ul+1):
        if perfect(i):
            print(i)
isperfect(1,50)'''


#palindrome or not 
'''def ispalindrome(n):
    dummy=n
    rev=0
    while n>0:
        rem=n % 10
        rev=rev*10+rem
        n//=10
    return rev==dummy
def palindrome(ll,ul):
    for i in range(ll,ul+1):
        if ispalindrome(i):
            print(i)
palindrome(1,50)  '''


#armstrong or not
'''def isarmstrong(n):
    dummy=n
    total=0
    l=len(str(n))
    while dummy>0:
        rem=dummy%10
        total=total+rem**l
        dummy//=10
    return total==n
def armstrong(ll,ul):
    for i in range(ll,ul+1):
        if isarmstrong(i):
            print(i)
armstrong(1,5000)'''

#harshad number

'''def isharshad(n):
    dummy=n
    total=0
    while dummy >0:
        rem=dummy%10
        total=total+rem
        dummy//=10
    return n % total ==0
def harshad(ll,ul):
    for i in range(ll,ul+1):
        if isharshad(i):
            print(i)
harshad(10,50)'''


#disram or not

def isdisram(n):
    s=str(n)
    total=0
    for i in range(len(s)):
        total=total+int(s[i]) ** (i+1)
    return total==n
def disram(ll,ul):
    for i in range(ll,ul+1):
        if isdisram(i):
            print(i)
disram(1,50)