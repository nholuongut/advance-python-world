from functools import reduce    

# lamda function

points2D = [(1,2) , (15,1),(5,-1),(10,4) ]
points2D_sorted = sorted( points2D , key = lambda x: x[1] )

print(points2D_sorted)

# map func
a = [ 1, 2 , 3 , 4 , 5,6]
b = map( lambda x: x+2 , a )
print(list(b) )

# filter func
def modulus(x):
    if x%2 ==0:
        return x
    
modul_2 = filter( lambda x: modulus(x=x) , a )
print(list(modul_2))

# reduce func
def multiply(x,y):
    return x * y

reduce_a = reduce(lambda x,y: multiply(x,y) , a)
print(reduce_a)