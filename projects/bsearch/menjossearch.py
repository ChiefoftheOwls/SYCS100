git commit
# hello teamates this is our file. add your code and comment your name

# Nolan English Code Follows

#TEST EDIT 2

import random

List = []

x = 10

while x >= 0:
    random.seed()
    List.append(random.randint(1,10))
    x -= 1

#TEST EDIT 2
import random
List = []
x = 10
while x >= 0:
    random.seed()
    List.append(random.randint(1,10))
    x -= 1
x = 10
def sorting(a,d):
    c = 0
    a.sort()
    print a
    for i in a:
        if i == d:
            c += 1
    if c == 0:
        print "the value %s is not in the list try again" % (str(d))
    elif c > 1:
        print "their is more than one instance of what you are looking for: %s" %(str(d)) 
    elif c == 1:
        b = ((len(a) - 1) / 2)
        endpoint = len(a) -1
        startpoint = 0 
        while True:
            if d >= a[b]:
                startpoint = b
                while True:
                    if d > a[endpoint - ((endpoint-startpoint)/2)]:
                        startpoint = (endpoint - ((endpoint-startpoint)/2))
                    if d < a[endpoint - ((endpoint-startpoint)/2)]:
                        endpoint = (endpoint - ((endpoint-startpoint)/2))
                    if d == a[endpoint - ((endpoint-startpoint)/2)]:
                        print "the value %s is at %s\n" % (str(a[endpoint - ((endpoint-startpoint)/2)]) ,str(endpoint - ((endpoint-startpoint)/2))) 
                        break
                    if d == a[startpoint]:
                        print "the value %s is at %s\n" % (str(a[startpoint]),str(startpoint))
                        break
                    if d == a[endpoint]:
                        print "the value %s is at %s\n" %(str(a[endpoint]),str(endpoint))
                        break
                break
            break
        while True:
            if d <= a[b]:
                endpoint = b
                while True:
                    if d > a[endpoint - ((endpoint-startpoint)/2)]:
                        startpoint = (endpoint - ((endpoint-startpoint)/2))
                    if d < a[endpoint - ((endpoint-startpoint)/2)]:
                        endpoint = (endpoint - ((endpoint-startpoint)/2))
                    if d == a[endpoint - ((endpoint-startpoint)/2)]:
                        print "the value %s is at %s\n" % (str(a[endpoint - ((endpoint-startpoint)/2)]) ,str(endpoint - ((endpoint-startpoint)/2))) 
                        break
                    if d == a[startpoint]:
                        print "the value %s is at %s\n" % (str(a[startpoint]),str(startpoint))
                        break
                    if d == a[endpoint]:
                        print "the value %s is at %s\n" % (str(a[endpoint]),str(endpoint))
                        break
                break
            break
        if d == a[b]:
            print "wow its exactly in the middle"

while x > 0:
    sorting(List,x)
    x -=1
    


# Nolan English CODE ends



#Hey Guys: Jahmaal Gayle @02661559 CODE

def ageSearch (ages, targetAge, bottomIndexes=0, topIndexes=5):
    if topIndexes is 5:
        topIndexes = len(ages)
    while bottomIndexes < topIndexes:
        middleIndexes = (bottomIndexes+topIndexes)//2
        middleNumber = ages[middleIndexes]
        if middleNumber < targetAge:
            bottomIndexes = middleNumber+1
        elif middleNumber > targetAge:
            topIndexes = middleIndexes
        else:
            return middleIndexes
    return -1
ages=(5,10,15,20,25,30)
targetAge=20
index=ageSearch(ages, targetAge, bottomIndexes=0, topIndexes=5)
print index

#Jahmaal Gayle code ends
#selina Jones code
mylist=[0,6,98,1,4,88,33,91,43,90,78]
 mylist.sort()
 mylist
 

 def bsearch(mylist,x):
     size=len(mylist)
     low=0
     high=size
     if mylist==[]:
         return mylist
     if high==size:
         high =len(mylist)-1
     while low<=high:
         mid = (low+high)/2
         midval=mylist[mid]
         if midval<x:
             low=mid+1
         elif midval>x:
             high=mid
         else:
             return mid
     return -1
             
 bsearch([0,6,98,1,4,88,33,91,43,90,78],0)
# Selina Jones code ends

#Oreoluwa Onatemowo's code starts
def bsearch(blist,searchElement):       
    blist.sort()
    if blist == []:
        return -1
    else:
        initial_index=0
        final_index = len(blist)-1
        while initial_index <= final_index:
            midpoint = (initial_index + final_index)/2
            if blist[midpoint] == searchElement:
                return len(blist)/2
            
            elif blist[midpoint]  > searchElement:
                final_index = midpoint+1
            elif blist[midpoint] < searchElement:
                initial_index = midpoint-1
            elif searchElement in blist != True:
                return -1

#Oreoluwa Onatemowo's code ends here
#Elyon Olaniran
List = [1, 2, 3, 5, 7, 8, 9, 12, 14, 15, 59, 61, 78, 84]
'''binary search only works on a sorted list. for the sake of this code.
I created a sorted List, hence no need to sort it again.'''
Element = 84
def bsearch(List, Element):
        if List == []:
                print 'empty list'
        else:
                x = len(List)
                q = 0
                first = 0
                last = x-1
                midpoint = (first + last)//2
                for q in range(x):
                        if Element == List[midpoint]:
                                return midpoint
                        elif Element < List[midpoint]:
                                last = midpoint-1
                                midpoint = (first+last)//2
                        elif Element > List[midpoint]:
                                first = midpoint + 1
                                midpoint = (first+last)//2
                        else:
                                return -1
print bsearch(List, Element)

#Elyon Olaniran code ends
