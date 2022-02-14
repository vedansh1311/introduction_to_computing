strng = input("Enter the string: ").lower().replace("."," ").replace(","," ").split()      #removing some commonly used special charecters if any
if len(strng) == 1:
    strng = strng[0]
occur = {}
for i in strng:                                       #taking each word/alphabet of sentence
    if i in occur:             #counting no.of times a word ocuured                  
        occur[i] += 1
    else:
        occur[i] = 1
print("The occurence(s) of:")
for i in occur:
    print("the word","'",i,"'","occurred", occur[i]," times")



#question 2

def ly(y):
  if (y % 400 == 0):
    leap_year = True
  elif (y % 100 == 0):
    leap_year = False
  elif (y % 4 == 0):
    leap_year = True
  else:
    leap_year = False
  return leap_year

while True:
 d=int(input("\nEnter the day"))
 m=int(input("Enter the month"))
 y=int(input("enter the year"))

 if (d < 1) or (d > 31) or (m < 1) or (m> 12) or (y < 1800) or (y> 2025):                  #Condition for given constraints in the question
        print("Please use the given conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")
        continue
 if m in (4,6,9,11) and d == 31:                                                                          #Condition for 31 days in a 30 day month
        print("The given month has only 30 days\nPlease enter a valid date")
        continue
 elif m == 2 and d>= 29:                                                                                 #Condition for no. of days in February
        if ly(y)==True and d!= 29:
            print("The given month has only 29 days\nPlease enter a valid date")
            continue
        else:
            print("The given month has only 28 days\nPlease enter a valid date")
            continue
 break

if m in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif m == 2:
    if ly(y)==True:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


if d < month_length:
    d += 1
else:
    d = 1
    if m == 12:
        m = 1
        y += 1
    else:
        m += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (d, m, y))


#question 3

lst=[]
lst1=[]
A=[]
X=[]
n = int(input("\nEnter number of elements : "))

def sq(a,i):
    X.append(a)
    n=a*a
    X.append(n)
    return X[2*i:]

for i in range(0, n):
   ele = int((input()))
   lst.append(ele)  # adding the element

for i in range(0,n):
   w=sq(lst[i],i)
   t=tuple(w)
   A.append(t)

print(A)


#question 4
g=int((input("\nenter your gpa")))
GP=["4","5","6","7","8","9","10"]
P=["Poor","Below","Average","Average","Good","Very Good","Excellent","Outstanding"]
LG=["D","C","C+","B","B+","A","A+"]
n=8
if(g<4 or g>10):
       {print("invalid gpa")}
else:
    for i in range(7):
        if (g==int(GP[i])):
          t=P[i]
          print("Your grade is","'",LG[i],"'", "and",P[i],"performance")


#question 5

n = 6
print("\n")
for i in range(n):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(n-i)-1):
        print(chr(65 + j), end='')
    print()



#question 6

dict1 = {}
while True:                                                                                                     
    name = input("Enter the name of the student: ")
    SID = int(input("Enter the SID of %s: " % name))
    dict1[SID] = name
    print("\nYou have entered %d value(s) till now" % len(dict1))
    while True:
        more_data = input("Do you want to enter more data? ")
        if more_data in ("N","n","No","no","NO"):
            more_data = 0
            break
        elif more_data in ("Y","y","Yes","yes","YES"):
            more_data = 1
            break
        else:
            print("\nPlease say yes or no")
            continue
    if more_data == 0:
        break
print("\na. Student Details:")                                                                              
for i in dict1:
    print("The SID %s is %d" % (dict1[i],i))
dict2 = {}
for sorted_value in sorted(dict1.values()):                                                                     
    for key,value in dict1.items():
        if value == sorted_value:
            dict2[key] = value
print("\nb. Student Details (sorted with respect to names):")                                       
for i in dict2:
    print("The SID of %s is %d" % (dict2[i],i))
dict3 = {}
for sorted_key in sorted(dict1):                                                                                
    for key,value in dict1.items():
        if key == sorted_key:
            dict3[key] = value
print("\nc. Student Details (sorted with respect to SIDs):")                                                        
for i in dict3:
    print("The SID of %s is %d" % (dict3[i],i))
print("\nd. ", end="")                                                                                          
while True:
    search_SID = int(input("Enter the SID of the student: "))
    if search_SID in dict1:
        print("The name of student whose SID is %d is %s" % (search_SID,dict1[search_SID]))
        break
    else:
        print("The SID you entered isn't entered\nPlease enter a valid SID to be searched\nList of valid SIDs: %s\n" % list((dict1.keys())))
        continue


#question 7

nterms = int(input("\n How many terms? "))
n1, n2 = 0, 1
count = 0
s=0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       s=s+n1
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
print("average",s/nterms)



#question 8

set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}
set4={1,2,3,4,5,6,7,8,9,10}

s1=set1.union(set2)
s2=set1.intersection(set2)
s4=set1.intersection(set3)
s5=set2.intersection(set3)
s6=set2.union(set3)
s7=s6.union(s1)

s3=s1.difference(s2)
print("a)",s3)   

s8=s2.union(s4)
s9=s8.union(s5)

s10=s1.union(s7)
s11=s10.difference(s9)
print("b)",s11)

print("c)",s9)

s12=set4.difference(set1)
print("d)",s12)















    
