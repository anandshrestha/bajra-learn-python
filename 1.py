"""principal=int(input("Enter the pricipal amount: "))
time=int(input("Enter the time(year): "))
rate=int(input("Enter the rate: "))
simple_interest=(principal*time*rate/100)
print("simple_interest: ", simple_interest)"""

x= int(input("Enter a number "))
y=int(input("Enter another number: "))
value=input("Enter character to perform mathmetical calculation: a,b,c,d: ")
if value=='a':
    value=(x+y);
    print(value)
elif value=='b':
    value=(x-y);
    print(value)
elif value=='c':
    value=(x/y);
    print(value)
else:
   value=x*y;
   print(value)
    