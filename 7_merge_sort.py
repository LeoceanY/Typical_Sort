# -*- coding:utf-8 -*-

# ref: http://python.jobbole.com/82270/
# merge sort.
#基本思想： 
class solution:
	#left,right 都已经是有序的了
	def merge(self,left,right):
		rk = []
		i,j = 0,0
		while  i<len(left) and j < len(right):
			if left[i] <= right[j]:
				rk.append(left[i])
				i = i+1
			else:
				rk.append(right[j])
				j = j+1
		rk += left[i:]
		rk += right[j:]
		return rk
	def merge_sort(self,lists):
		if len(lists)<=1:
			return lists
		mid = len(lists)/2
		left = self.merge_sort(lists[:mid])
		right = self.merge_sort(lists[mid:])
		return self.merge(left,right)

if __name__ == '__main__':
	s=solution()
	list1 = [1,3,4,5,9,1,5,2,11,3]
	print s.merge_sort(list1)

