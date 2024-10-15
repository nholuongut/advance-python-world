# Using the generator pattern (an iterable) 
####### define custom iterator #########
from itertools import takewhile

class first_n(object):
 
     def __init__(self, n):
         self.n = n
         self.num = 0

     def __iter__(self):
         return self

     # Python 3 compatibility
     def __next__(self):
         return self.next()

     def next(self):
         if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
         raise StopIteration()
     

###### python support generator functions which acts as a iterable object
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

######  we can turn a list comprehension into a generator expression by replacing the square brackets ("[ ]") with parentheses. ######
"""
y= [x*x for i in range(100)]

y_gen = (x*x for i in range(100))

"""

#### 

 
if __name__== '__main__':

    sum_of_first_n = sum(first_n(1000000))
    print( "result with custom iterator : " , sum_of_first_n)
    
    sum_of_first_n_gen = sum( firstn_generator(1000000) )
    print("result of the generator function" , sum_of_first_n_gen)

    #add squares less than 100
    square = (i*i for i in range(1000))

    """
    internel of the takewhile

    def takewhile(predicate, iterable):
        for i in iterable:
            if predicate(i):
                    return(i)
            else:
                    break
    
    """

    bounded_squares = takewhile(lambda x : x< 100, square)
    total = 0

    for i in bounded_squares:
        total += i

    print(total)

    