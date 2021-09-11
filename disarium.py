#Python program to check if the given number is a Disarium Number

x=int(input("emter ther number "))
print(x)

def get_digits(x):             # to get no.of digit in a number 
    num=x
    z=1
    a=0
    while z!=0:
        z=num//(10**(a+1))
        a=a+1
    print('no. of digit in numbber is :',a)
    return a

a=get_digits(x)
print(a)
number=x
sum=0
while(a!=0):
    digit=x%10
    print('digit is ',digit)
    sum=sum+(digit**a)
    print('sum becomes',sum)
    a=a-1
    x=x//10
    print("now no. is ",x)


if (sum==number):
    print('no. is disarium number')
