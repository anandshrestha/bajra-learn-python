name = ["ram","hari" , "shyam"]
print(name[-1])


name=["ram","hari","james"]
name[1]="jam"
print(name)





# difference between tuples and list 
# return the collection of leap year from the collection of years between [2000, 2030]



#Using Iteration
input=list(range(2000,2030))
list.count(input)
def checkleapyears (years):
    return (((years % 4 == 0) and (years % 100 != 0)) or (years % 400 ==0))
Answer = 0
for y in input:
    if checkleapyears(y):
        Answer = Answer+1
print("number of leap years are: ", Answer)
print(Answer)
list.count(y)