#Maimuna Ahmed's code starts hur
def bsearch( alist , element):
	alist.sort()
	front = 0
	back = len(alist)-1
	found = True
	midpoint = (front + back)//2

	for i in range(len(alist)):

		if alist[midpoint] == element:
			return midpoint

		elif element > alist[midpoint]:
			front = midpoint + 1
			midpoint = (front + back)//2

		elif element < alist[midpoint]:
			back = midpoint - 1
			midpoint = (front + back)//2

	return -1
#Maimuna Ahmed's code ends hur
#Selina Jones git-jayenator565 bsearch code


def bsearch(mylist,x):
    mylist.sort()	
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

#selina's code ends here
#Elyon Olaniran code starts here
'''binary search only works on a sorted list. for the sake of this code.
only a sorted list should be given as a parameter for the function bsearch'''
def bsearch(List, Element):
        if List == []:
                #print 'empty list'
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
                        #else:
                 return -1
#Elyon Olaniran Code ends here
