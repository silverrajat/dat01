   # -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 20:59:06 2019

@author: DELL
"""

n=5
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')
    
for i in range(n):
    for j in range(5-i):
     print('* ', end="")
    print('')


str1="hello,world"
str1.index("o")

word=input("enter word-")
for i in word:
    print(i)

#list
Avengers=["hulk","iron man","captain america","thor","natash"]
Avengers[2]="nat-natasha" 
Avengers
Avengers1=["vision","panther"]
Avengers2=Avengers+Avengers1
Avengers2
if "iron man" in Avengers:
    print("yes")
max(Avengers)
list=[1,123,2,3,4,5,56,45,345.0,7,345]
max(list)


tup=('a','b','c')
list= (tup)
list

list1=[2,3,5,2,3,9,6,8,1]
sorted(list1)
tup1=(2,3,4,1,8,5,7,3,0)
sorted(tup1)

Avengers5=[]
Avengers.append("captain america")
Avengers5
Avengers.append("iron man")
Avengers5

Avengers.extend(Avengers1)
Avengers


list=["mohit","tata"]
name="rajat"
list.extend(name)
list




def Remove(dupicate):
    list=[]
    for num in duplicate:
        if num  not in list:
            list.append(num)
            return list
duplicate=[2,2,34,5,6,6,7,8,9,8]
print(Remove(duplicate))


#list1=[1,2,3,6,6,5,5,5,4,8,6,7,8,9]
#list2=[]
#for i in list1:
#    list2.append(list1)
#print(list2)
num=float(input("enter number:"))
if num>=4:
    letter="A"
elif num>=3:
    letter="B"
elif num>=2:
    letter="C"
else :
    letter="D"
print("the grade is ",letter)

for count in range(4):
    print(count)
    
product=2
for i in range(1,9):
    j=(product+4)/2
    product=product+j
    print(product)
for i in "rajat":
    print(i)

checking_acc=4
num=int(input("enter account number:"))
while checking_acc!= num:
    print("wrong number")
    num=int(input("enter right number"))
print("*****")
print("your acc num is ",num)



suum=0
for i in range(1,10):
    suum=suum+i
    print(suum)
    
sum=0
i=1
while(i<10):
    sum=sum+i
    print(sum)
    i=i+1
sum=0
while True:
    data=(int(input("enter a data or press o to quit:")))
    if data==0:
        break
    sum= sum+data
print("sum is ",sum)

  
            
movies=['avengers','ps i love you','hitman','jason bourn','fast','jumanji']
for i in movies:
    if i==('hitman'):
        break
    print(i)

"".


"".join(Reversed("rajat"))


"rajat"[::-1]
def name(rajat):
    return rajat[::-1]


movies={"iron":"tony","thor":"loard",:"captain":"steve",}
movies1=[]





temp={'t1':-34,'t2':-28,'t3':20,'t4':-17}

c_temp={k:v*9/5+35 for (k,v) in temp.items()}
print(c_temp)

print("name","age","designation","salary")
print("%s %9d %4s %13.2f" % ("jone deo",35,"senior Manager",10.65))


a=2
b=3
x=complex(a,b)
print(x)


s1=10
s2=12
s3=17.5
T_side=(s1+s2+s3)/2
t_area=(T_side*(T_side-s1)*(T_side-s2)*(T_side-s3))**0.5
print(t_area)

r=5
pi=3.14
area=pi*(r**2)
print(area)

str1="my name is rajat"
str2="my name is rajat prakash"
print(str1 in str2 )

arre1=(1,2,3)
arre2=(1,2,4)
print(5 in arre1)

str1=input("enter a string:")
str2=[]
for i in str1: str2.append[::-1]
print(str2)

p="rajat"
q=reversed(p)
print(q)

in_str=input("enter a string")
in_str=in_str.casefold()
rev_in_str=reversed(in_str)
if list(in_str)==list(rev_in_str):
    print("input string is palindrome")
else:
    print("input string is not oalindrome")

print("a")
print("\t\trajat")
print("i know , he is good")
print("only way to join"+"two string")

print("name","age","marks")
print("%s %8d %2.2f" % ("john deo",34,68.85))
print("%s %3d %2.2f" % ("rajat prakash",23,89.98))


str=input("enter a string:")
word=str.split(" ")
str.sort()
for i in str:
    print(i)


num="jone"
num[1]

num=int(input("enter a number:"))
num1=len(str(num))
sum=0
a=num
while num>0:

    dg=num%10
    sum=sum+dg**num1
    num=num//10
    print(dg)
    print(sum)
    print(num)
if a==sum:
    print("number is armstrong number")
else:
    print("number is not armstrong number")



num=int(input("enter a number:"))
a=num
fact=1
sum=0
while num>0:
    dg=num%10
    fact=1
    for i in range(1,dg+1):
        fact=fact*i
    sum=sum+fact
    num=num//10
    print(dg)
    print(fact)
    print(sum)
if sum==a:
    print("number is krishnamurthy number")
else:
    print("number is not krishanamurthy number")



list1=int(input("enter a number:"))
min=list1
for i in list1:
    if i<min:
        min=i
        return min


list2=int(input("enter numbers:"))
a=list2
min(a)
list3=int(input("enter a mu:"))
def smallest (list3):
    min=list3
    for i in list3:
        if i<min:
            min=i
        return min
        




























                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           