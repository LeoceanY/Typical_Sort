class parants(object):
	a = 1

class child1(parants):
	pass
class child2(parants):
	pass

print parants.a,child1.a,child2.a

child1.a = 2

print parants.a,child1.a,child2.a

parants.a = 3
print parants.a,child1.a,child2.a

list1 = [1,2,3,4,5,6,7,8,9,0]

print list1[::2]

list2 = [i for i in list1[::2] if i%2==1]

print list2


#def funcs(a,list=[]):
#	list.append(a)


#print ("%s"%funcs(10))
#print ("%s"%funcs(125,list=[]))
#print ("%s"%funcs(list=[]))
<html> <tag> <dd> <ss> </a>