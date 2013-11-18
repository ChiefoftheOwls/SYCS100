#This file is on behalf of the following individuals.
#Maimuna Ahmed
#Elyon Olaniran
#Selina Jones
#Oreoluwa Onatemowo
#Nolan English
#Jamal Gayle
  #Elyon Olaniran's Code starts here
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

#Elyon's Code Ends here
