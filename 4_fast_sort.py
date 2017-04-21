# -*- coding:utf-8 -*-
# ref: http://python.jobbole.com/82270/
# fast sort.
#基本思想： 
  
class solution:
	def fast_sort(self,list_orig,left,right):
		if left >= right:
			return list_orig
		key = list_orig[left]
		i = left
		j = right
		while i < j:
			while i < j and list_orig[j] >= key:
				j = j-1
			list_orig[i] = list_orig[j]
			while i < j and list_orig[i] <= key:
				i = i+1
			list_orig[j] = list_orig[i]
			list_orig[i] = key
		print list_orig
		self.fast_sort(list_orig,left,i-1)
		self.fast_sort(list_orig,i+1,right)
		return list_orig

	def quick_sort(self,lists, left, right):
		# 快速排序
		if left >= right:
			return lists
		key = lists[left]
		low = left
		high = right
		while left < right:
			while left < right and lists[right] >= key:
				right -= 1
			lists[left] = lists[right]
			while left < right and lists[left] <= key:
				left += 1
			lists[right] = lists[left]
		lists[right] = key
		print lists
		self.quick_sort(lists, low, left - 1)
		self.quick_sort(lists, left + 1, high)
		return lists

if __name__ == '__main__':
	s=solution()
	list1 = [1,4,8,3,9,3,4,2,89,6,23,1]
	l = len(list1)
	#print s.quick_sort(list1,0,l-1)	
	print s.fast_sort(list1,0,l-1)

