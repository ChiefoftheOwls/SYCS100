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


#Elyon Olaniran's code starts here
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
''' this code creates a function the prints out 'empty list' if the list has no contents. if it does, it then sets the
first index of the list to the variable first and the last index to teh variable last. it then takes the midpoint of the
midpoint of the list and checks if it is the element being searched for. if it is, it returns the index. if not it it
checks if the upper segment is a possible location for seach element and then conducts the midpoint expression. else it
checks the lower segment and does the same thing. if the element is not found it returns -1'''

# Elyon Olaniran's code ends here
