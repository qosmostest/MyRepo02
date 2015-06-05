#! python
# work with lists

a = ['spam', 'eggs', 100, 1234]
print " list a=",a

# list indices start at 0, 
print 'a[0]=', a[0]

print 'a[3]=', a[3]
print 'a[-2]=', a[-2]

# lists can be sliced, concatenated and so on: 
print  "a[1:-1]=", a[1:-1]

print a[:2] + ['bacon', 2*2]

print 3*a[:3] + ['Boe!']

# possible to change individual elements of a list: 

a[2] = a[2] + 23
print "changing a[2]=", a

#Assignment to slices is also possible, and this can even change the size of the list: 

# Replace some items:
a[0:2] = [1, 12]
print a

# Remove some:
a[0:2] = []
print a

# Insert some:
a[1:1] = ['bletch', 'xyzzy']
print a

a[:0] = a     # Insert (a copy of) itself at the beginning
print a

print "length=", len(a)

# possible to nest lists (create lists containing other lists) 

q = [2, 3]
p = [1, q, 4]
print " nest list=", p

print 'length =', len(p)

print p[1]

print p[1][0]

p[1].append('xtra')  
print p

print q
