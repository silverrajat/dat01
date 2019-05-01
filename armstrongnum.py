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
