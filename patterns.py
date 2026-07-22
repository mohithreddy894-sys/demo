#without using function
'''n=int(input("enter a number"))
for row in range(1,n+1):
    for col in range(1,row+1):
        print("*",end=" ")
    print()'''
'''
*
* *
* * *
* * * *
'''

#using function
'''def triangle(n):
    for row in range(1,n+1):
        for col in range(1,row+1):
            print("*",end=" ")
        print()
def main():
    n=int(input("enter"))
    triangle(n)
if __name__=="__main__":
    main()'''


# using function without
'''
1
1 2
1 2 3
1 2 3 4
'''
'''n=int(input("enter"))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()'''

#using function
'''def number(n):
    for row in range(1,n+1):
        for col in range(1,row+1):
            print(col,end=" ")
        print()
def main():
    n=int(input("enter"))
    number(n)
if __name__=="__main__":
    main()'''

# without function
'''
1
2 3
4 5 6
7 8 9 10
'''
'''n=int(input("enter"))
num =1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num ,end=" ")  
        num+=1
    print()'''
#using function
'''def cnumber(n):
    num=1
    for row in range(1,n+1):
        for col in range(1,row+1):
            print(num ,end=" ")
            num+=1
        print()
def main():
    n=int(input("enter"))
    cnumber(n)

if __name__=="__main__":
    main()      '''


#without function
'''
* * * *
* * *
* *
*
'''
'''n=int(input("enter"))
for row in range(n,0,-1):
    for col in range(1,row+1):
        print("*",end=" ")
    print()'''

#with function
'''def reverse(n):
    for row in range(n,0,-1):
        for col in range(1,row+1):
            print("*",end=" ")
        print()
def main():
    n=int(input("enter"))
    reverse(n)
if __name__=="__main__":
    main()'''

#with out functions
'''
   *
  * *
 * * *
* * * *

'''
'''n=int(input("enter"))
spaces=n-1
stars=1

for row in range(1,n+1):
    for sp in range (1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    stars+=2
    spaces-=1'''

#with functions
'''def pyramid(n):
    spaces=n-1
    stars=1
    for row in range(1,n+1):
        for sp in range(1,spaces+1):
            print(" ",end=" ")
        for st in range(1,stars+1):
            print("*",end=" ")
        print()
        spaces-=1
        stars+=2
def main():
    n=int(input("enter"))
    pyramid(n)
if __name__=="__main__":
    main()'''

#
'''def pyramid(n):

    spaces = n - 1
    stars=1

    for row in range(1, n + 1):

        for sp in range(1, spaces + 1):

            print(" ", end=" ")

        for star in range(1, stars + 1):

            print("*", end=" ")

        print()

        spaces -= 1
        stars+=2
def main():
    n=int(input("enter"))
    pyramid(n)
if __name__=="__main__":
    main()'''


'''n=int(input("enter"))
spaces=n//2
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        if st==1 or st==stars:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    if row <= n//2 :
        stars+=2
        spaces-=1
    else:
        stars-=2
        spaces+=1'''

'''import math
n=23
mid=n//2
grid=[[' 'for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        x=i-mid
        y=j-mid
        r=math.sqrt(x*x+y*y)
        theta=math.atan2(y,x)
        if r<=8+math.sin(4 + theta):
            grid[i][j]='*'
for i in range(mid,n):
    grid[i][mid]='|'

leaves=[(mid+6,mid-3),(mid+10,mid+3)]
for (x,y) in leaves:
    grid[x][y]='/'
    grid[x][y+1]='\\'
for row in grid:
    print(' '.join(row))'''
