# -*- coding:utf-8 -*-

# ref: http://python.jobbole.com/82270/
# insert sort.
#基本思想： 
#	插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，
#从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。
#是稳定的排序方法。插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，
#但将最后一个元素除外（让数组多一个空间才有插入的位置），而第二部分就只包含这一个元素
#（即待插入元素）。在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。

class solution:
	def insert_sort(self,list_orig):
		l = len(list_orig)
		for i in range(1,l):
			key = list_orig[i]
			j = i
			#相当于进行一次冒泡排序，使得key数据能够插入到正确的位置。
			while j>0: 
				if list_orig[j]<list_orig[j-1]:
					list_orig[j] = list_orig[j-1]
					list_orig[j-1] = key
				j = j - 1
		return list_orig

if __name__ == '__main__':
	s=solution()
	list1 = [1,3,4,5,9,1,5,2,11,3]
	print s.insert_sort(list1)

