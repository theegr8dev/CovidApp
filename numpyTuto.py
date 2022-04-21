'''
Basic tutorial on numpy libray

.itemsize is use to check for the byte size
axis = 0 >>> column
axis = 1 >>> row
'''
import numpy as np
from matplotlib import pyplot as plt

SA = np.array([1,2,3]) # creating one dimension array
MA = np.array([[1,2], [3,4], [5,6]]) # creating mmultiy dimension array
checkDimension = MA.ndim # check the dimension of the array

# chaning array datatype
MA2 = np.array([[1,2,3], [3,4,5], [6,7,8]], dtype=np.float64)

# generate arrys of specific number
zeros = np.zeros((3,4))
ones = np.ones((10,5))

# range of number
range = np.arange(10)

#----------------------- Characters-------------------
add = np.char.add(['hello ', 'hi '], ['Khalid', 'Alabi']) # concat the first array ewith the second ..

multiply = np.char.multiply(('hello ', 'hi '), 3) # multiply array by the specified number

center = np.char.center(('hello'), 20, fillchar = '-') # spacing the array with the specified number and adding the filling the whitespaces..


#----------------------Array Manipulations..---------------------------
a = np.arange(12)

b = a.reshape(4,3) # turning a single dimensional array to multiply ..

c = b.flatten() # turning the multiply dimensional array to a single array
d = b.flatten(order='F') # order the flatten(single dimensional array) in a column major

e = np.transpose(b) # turn rows to columns and columns to rows

f = c.reshape(3,2,2) # 3 set of multi dimensional array with 2 rows and columns

# print('------------------------------------------------------------------')
'''
rollaxis and swapaxes
'''

#----------------------Array Operations..---------------------------
g = np.arange(9).reshape(3,3)

h = np.array((10,20,20))

i = np.add(g,h) # add the array row by row--> same as(subtract, divide, multiply)

#----------------------Iterating..-------------------------
k = np.arange(0,50,5).reshape(5,2) # 0 to 50 step 5--> same as slicing---> slice(2,12,3) >>> a[s]

for l in np.nditer(k):
    # print(l)
    pass

for m in np.nditer(k, order='F'): # itering through the array through column major
    #print(m)
    pass
    

#----------------------Joining arrays..-------------------------
m = np.array([[1,2,3], [4,5,6]])
# print('first array')

n = np.array(((7,8,9),(10,11,12)))
#print('second array')

# print('joining the 2 arrays along axis 0: ')
o = np.concatenate((m, n), axis = 0) #concat with column

# print('joining the 2 arrays along axis 1: ')
o = np.concatenate((m, n), axis = 1) #concat with rows

#----------------------Spliting arrays..-------------------------
p = np.arange(20)
q = np.split(p, 5)

#----------------------Numpy histogram using matplotlib..-------------------------
r = np.array([20, 87, 4, 40, 53, 74, 56, 51,11,20,40,15,79,25,27])

# plt.hist(r, bins = [0,20,40,60,80,100])
# plt.title('histogram')
# plt.show()

#----------------------Numpy histogram using matplotlib..-------------------------
sx = np.arange(0, 3*np.pi, 0.1)
ty = np.sin(sx)

# plt.plot(sx,ty)
# plt.show()